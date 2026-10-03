DEFAULT_RULES=[{'rule_id':'R001','name':'Excessive Connection Rate','threshold':30},{'rule_id':'R002','name':'Repeated Failed Connections','threshold':.45},{'rule_id':'R003','name':'High Destination Port Activity','threshold':12},{'rule_id':'R004','name':'SYN Heavy Behavior','threshold':.55},{'rule_id':'R005','name':'Unusual Service Port Activity','threshold':1},{'rule_id':'R006','name':'High Traffic Volume','threshold':2500000}]
def analyze_flow(flow,f=None,rules=None):
    f=f or {}; rules=rules or DEFAULT_RULES; m=[]
    if f.get('connection_rate',0)>=rules[0]['threshold']: m.append(('R001','Excessive connection rate',30))
    if f.get('failure_ratio',0)>=rules[1]['threshold']: m.append(('R002','Repeated failed connections',25))
    if f.get('connection_count',0)>=rules[2]['threshold']: m.append(('R003','High destination port/connection activity',20))
    if f.get('syn_ratio',0)>=rules[3]['threshold']: m.append(('R004','SYN-heavy behavior',25))
    if int(f.get('destination_port',0)) in {23,4444,5555,31337,9001}: m.append(('R005','Unusual service-port activity',20))
    if f.get('byte_count',0)>=rules[5]['threshold']: m.append(('R006','High traffic volume',20))
    return m
