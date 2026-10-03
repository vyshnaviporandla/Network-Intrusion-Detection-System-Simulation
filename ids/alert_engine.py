from datetime import datetime,timezone
def severity_from_risk(r): return 'CRITICAL' if r>=81 else 'HIGH' if r>=61 else 'MEDIUM' if r>=41 else 'LOW' if r>=21 else 'INFO'
def build_alert(flow,matches,anomaly,risk,classification):
    if risk<=20 and not matches:return None
    x=matches[0] if matches else ('ANOMALY','Statistical anomaly detected',0)
    return {'timestamp':datetime.now(timezone.utc).isoformat(),'source_ip':flow['source_ip'],'destination_ip':flow['destination_ip'],'protocol':flow['protocol'],'source_port':flow['source_port'],'destination_port':flow['destination_port'],'rule_id':x[0],'alert_type':x[1],'severity':severity_from_risk(risk),'risk_score':risk,'classification':classification,'description':'Synthetic flow requires defensive investigation based on one or more detection signals.','status':'NEW'}
