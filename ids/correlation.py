from collections import defaultdict
def correlate_alerts(alerts,window_seconds=300):
    g=defaultdict(list)
    for a in alerts:g[(a.get('source_ip'),a.get('alert_type'))].append(a)
    return [{'source_ip':k[0],'alert_type':k[1],'alert_count':len(v),'incident_type':'CORRELATED_SECURITY_EVENT'} for k,v in g.items() if len(v)>=2]
