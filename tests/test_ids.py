from ids.feature_extractor import extract_network_features
from ids.rule_engine import analyze_flow
from ids.anomaly_detector import calculate_anomaly_score
from ids.risk_engine import calculate_risk
from ids.alert_engine import severity_from_risk
def sample(**x):
    d={'source_ip':'192.0.2.10','destination_ip':'198.51.100.10','source_port':50000,'destination_port':22,'protocol':'TCP','packet_count':100,'byte_count':50000,'duration_seconds':1,'connection_count':50,'failed_connection_count':30,'syn_count':70,'rst_count':10,'average_packet_size':500};d.update(x);return d
def test_features():
    f=extract_network_features(sample());assert f['failure_ratio']==.6 and f['connection_rate']==50
def test_rules():
    f=extract_network_features(sample());m=analyze_flow(sample(),f);assert any(x[0]=='R001' for x in m) and any(x[0]=='R002' for x in m)
def test_anomaly():assert 0<=calculate_anomaly_score(extract_network_features(sample()))<=100
def test_risk():assert calculate_risk([],50,None)[1]=='SUSPICIOUS'
def test_severity():assert [severity_from_risk(x) for x in [90,70,50,30,10]]==['CRITICAL','HIGH','MEDIUM','LOW','INFO']
