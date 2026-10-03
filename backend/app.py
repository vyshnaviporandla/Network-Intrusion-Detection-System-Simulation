from pathlib import Path
import sqlite3,sys
from flask import Flask,request,jsonify
from flask_cors import CORS
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from ids.feature_extractor import extract_network_features
from ids.rule_engine import analyze_flow,DEFAULT_RULES
from ids.anomaly_detector import calculate_anomaly_score
from ids.risk_engine import calculate_risk
from ids.alert_engine import build_alert
from ml.predict import predict_ml
DB=ROOT/'data'/'ids.db'; app=Flask(__name__); CORS(app)
def db():
    DB.parent.mkdir(exist_ok=True); c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init_db():
    c=db(); c.executescript('''CREATE TABLE IF NOT EXISTS network_flows(flow_id TEXT PRIMARY KEY,timestamp TEXT,source_ip TEXT,destination_ip TEXT,source_port INTEGER,destination_port INTEGER,protocol TEXT,packet_count INTEGER,byte_count INTEGER,duration_seconds REAL,connection_count INTEGER,failed_connection_count INTEGER,syn_count INTEGER,rst_count INTEGER,average_packet_size REAL,label TEXT,scenario_type TEXT,risk_score REAL,classification TEXT,anomaly_score REAL,ml_score REAL); CREATE TABLE IF NOT EXISTS alerts(alert_id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp TEXT,flow_id TEXT,source_ip TEXT,destination_ip TEXT,protocol TEXT,source_port INTEGER,destination_port INTEGER,rule_id TEXT,alert_type TEXT,severity TEXT,risk_score REAL,description TEXT,status TEXT,anomaly_score REAL,ml_score REAL,classification TEXT); CREATE TABLE IF NOT EXISTS incident_notes(id INTEGER PRIMARY KEY AUTOINCREMENT,alert_id INTEGER,note TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS rules(rule_id TEXT PRIMARY KEY,name TEXT,threshold REAL,enabled INTEGER DEFAULT 1);''')
    for r in DEFAULT_RULES:c.execute('INSERT OR IGNORE INTO rules(rule_id,name,threshold) VALUES(?,?,?)',(r['rule_id'],r['name'],r['threshold']))
    c.commit();c.close()
def process(flow):
    f=extract_network_features(flow); matches=analyze_flow(flow,f); anomaly=calculate_anomaly_score(f); ml=predict_ml(flow); risk,classification=calculate_risk(matches,anomaly,ml); flow.update(risk_score=risk,classification=classification,anomaly_score=anomaly,ml_score=ml); alert=build_alert(flow,matches,anomaly,risk,classification); c=db(); c.execute('INSERT OR REPLACE INTO network_flows VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(flow['flow_id'],flow['timestamp'],flow['source_ip'],flow['destination_ip'],flow['source_port'],flow['destination_port'],flow['protocol'],flow['packet_count'],flow['byte_count'],flow['duration_seconds'],flow['connection_count'],flow['failed_connection_count'],flow['syn_count'],flow['rst_count'],flow['average_packet_size'],flow['label'],flow['scenario_type'],risk,classification,anomaly,ml));
    if alert:c.execute('INSERT INTO alerts(timestamp,flow_id,source_ip,destination_ip,protocol,source_port,destination_port,rule_id,alert_type,severity,risk_score,description,status,anomaly_score,ml_score,classification) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(alert['timestamp'],flow['flow_id'],alert['source_ip'],alert['destination_ip'],alert['protocol'],alert['source_port'],alert['destination_port'],alert['rule_id'],alert['alert_type'],alert['severity'],alert['risk_score'],alert['description'],alert['status'],anomaly,ml,classification))
    c.commit();c.close();return flow,alert
@app.get('/api/health')
def health():return jsonify(status='healthy',project='Network IDS Simulation')
@app.post('/api/flows')
def create_flow():return jsonify(process(request.get_json(force=True))[0]),201
@app.get('/api/flows')
def flows():
    c=db();x=c.execute('SELECT * FROM network_flows ORDER BY timestamp DESC LIMIT 100').fetchall();c.close();return jsonify([dict(r) for r in x])
@app.get('/api/flows/<fid>')
def one_flow(fid):
    c=db();x=c.execute('SELECT * FROM network_flows WHERE flow_id=?',(fid,)).fetchone();c.close();return (jsonify(dict(x)),200) if x else (jsonify(error='Flow not found'),404)
@app.get('/api/alerts')
def alerts():
    c=db();x=c.execute('SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 100').fetchall();c.close();return jsonify([dict(r) for r in x])
@app.get('/api/alerts/<int:aid>')
def one_alert(aid):
    c=db();x=c.execute('SELECT * FROM alerts WHERE alert_id=?',(aid,)).fetchone();n=c.execute('SELECT * FROM incident_notes WHERE alert_id=?',(aid,)).fetchall();c.close();
    if not x:return jsonify(error='Alert not found'),404
    r=dict(x);r['notes']=[dict(v) for v in n];return jsonify(r)
@app.put('/api/alerts/<int:aid>/status')
def set_status(aid):
    s=request.get_json(force=True).get('status');
    if s not in {'NEW','INVESTIGATING','RESOLVED','FALSE_POSITIVE'}:return jsonify(error='Invalid status'),400
    c=db();c.execute('UPDATE alerts SET status=? WHERE alert_id=?',(s,aid));c.commit();c.close();return jsonify(status=s)
@app.post('/api/alerts/<int:aid>/notes')
def add_note(aid):
    note=request.get_json(force=True).get('note','').strip();
    if not note:return jsonify(error='Note required'),400
    c=db();c.execute('INSERT INTO incident_notes(alert_id,note) VALUES(?,?)',(aid,note));c.commit();c.close();return jsonify(message='Note added'),201
@app.get('/api/dashboard/stats')
def stats():
    c=db(); q=lambda s:c.execute(s).fetchone()[0]; total=q('SELECT COUNT(*) FROM network_flows'); normal=q("SELECT COUNT(*) FROM network_flows WHERE classification='NORMAL'"); suspicious=total-normal; open_=q("SELECT COUNT(*) FROM alerts WHERE status IN ('NEW','INVESTIGATING')"); critical=q("SELECT COUNT(*) FROM alerts WHERE severity='CRITICAL'"); avg=c.execute('SELECT COALESCE(AVG(risk_score),0) FROM network_flows').fetchone()[0];c.close();return jsonify(total_flows=total,normal_traffic=normal,suspicious_traffic=suspicious,open_alerts=open_,critical_alerts=critical,average_risk_score=round(avg,2))
@app.get('/api/dashboard/traffic')
def traffic():
    c=db();x=c.execute("SELECT substr(timestamp,1,16) bucket,COUNT(*) total,SUM(CASE WHEN classification='NORMAL' THEN 1 ELSE 0 END) normal,SUM(CASE WHEN classification!='NORMAL' THEN 1 ELSE 0 END) suspicious FROM network_flows GROUP BY bucket ORDER BY bucket DESC LIMIT 24").fetchall();c.close();return jsonify([dict(r) for r in reversed(x)])
@app.get('/api/dashboard/alerts')
def breakdown():
    c=db();sev=c.execute('SELECT severity,COUNT(*) count FROM alerts GROUP BY severity').fetchall();typ=c.execute('SELECT alert_type,COUNT(*) count FROM alerts GROUP BY alert_type ORDER BY count DESC LIMIT 10').fetchall();pro=c.execute('SELECT protocol,COUNT(*) count FROM network_flows GROUP BY protocol').fetchall();c.close();return jsonify(severity=[dict(x) for x in sev],types=[dict(x) for x in typ],protocols=[dict(x) for x in pro])
@app.get('/api/rules')
def rules():
    c=db();x=c.execute('SELECT * FROM rules').fetchall();c.close();return jsonify([dict(r) for r in x])
if __name__=='__main__':init_db();app.run(host='127.0.0.1',port=5000,debug=True)
