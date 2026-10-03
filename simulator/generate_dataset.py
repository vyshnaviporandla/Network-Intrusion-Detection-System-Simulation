from pathlib import Path
import ipaddress, random
from datetime import datetime,timedelta,timezone
import pandas as pd
random.seed(42)
NETWORKS=[ipaddress.ip_network(x) for x in ['192.0.2.0/24','198.51.100.0/24','203.0.113.0/24']]
SCENARIOS=['NORMAL_WEB','NORMAL_DNS','NORMAL_SSH','NORMAL_EMAIL','NORMAL_DATABASE','HIGH_CONNECTION_RATE','REPEATED_FAILED_CONNECTIONS','MULTI_PORT_PROBING_PATTERN','SYN_HEAVY_PATTERN','UNUSUAL_PORT_ACTIVITY','HIGH_TRAFFIC_VOLUME']
def random_ip(): return str(random.choice(list(random.choice(NETWORKS).hosts())))
def make_flow(i,scenario=None,timestamp=None):
    scenario=scenario or random.choices(SCENARIOS,weights=[24,12,7,7,6,8,7,7,7,6,9])[0]
    timestamp=timestamp or datetime.now(timezone.utc)-timedelta(seconds=random.randint(0,86400))
    src,dst=random_ip(),random_ip()
    while dst==src: dst=random_ip()
    normal={'NORMAL_WEB':(random.choice([80,443]),'TCP'),'NORMAL_DNS':(53,'UDP'),'NORMAL_SSH':(22,'TCP'),'NORMAL_EMAIL':(random.choice([25,465,587,993]),'TCP'),'NORMAL_DATABASE':(random.choice([1433,3306,5432]),'TCP')}
    if scenario in normal:
        dport,proto=normal[scenario]; packets=random.randint(8,120); duration=random.uniform(.2,15); connections=random.randint(1,5); failed=random.randint(0,1); syn=random.randint(1,3); rst=random.randint(0,2); avg=random.randint(300,1400)
    elif scenario=='HIGH_CONNECTION_RATE':
        dport,proto=random.choice([22,80,443,3389]),'TCP'; packets=random.randint(20,160); duration=random.uniform(.05,1.5); connections=random.randint(80,240); failed=random.randint(2,25); syn=random.randint(20,100); rst=random.randint(2,20); avg=random.randint(200,900)
    elif scenario=='REPEATED_FAILED_CONNECTIONS':
        dport,proto=random.choice([22,3389,3306]),'TCP'; packets=random.randint(5,80); duration=random.uniform(.1,5); connections=random.randint(10,70); failed=random.randint(8,55); syn=random.randint(4,35); rst=random.randint(5,25); avg=random.randint(100,900)
    elif scenario=='MULTI_PORT_PROBING_PATTERN':
        dport,proto=random.randint(1,65535),'TCP'; packets=random.randint(2,50); duration=random.uniform(.05,3); connections=random.randint(15,80); failed=random.randint(5,60); syn=random.randint(10,60); rst=random.randint(5,30); avg=random.randint(80,700)
    elif scenario=='SYN_HEAVY_PATTERN':
        dport,proto=random.choice([22,80,443,8080]),'TCP'; packets=random.randint(30,180); duration=random.uniform(.05,2); connections=random.randint(20,100); failed=random.randint(5,35); syn=random.randint(30,170); rst=random.randint(5,60); avg=random.randint(100,800)
    elif scenario=='UNUSUAL_PORT_ACTIVITY':
        dport,proto=random.choice([23,4444,5555,31337,9001]),random.choice(['TCP','UDP']); packets=random.randint(10,120); duration=random.uniform(.1,8); connections=random.randint(3,25); failed=random.randint(0,12); syn=random.randint(2,25); rst=random.randint(0,10); avg=random.randint(100,1200)
    else:
        dport,proto=random.choice([80,443,8080]),'TCP'; packets=random.randint(500,6000); duration=random.uniform(1,30); connections=random.randint(5,40); failed=random.randint(0,8); syn=random.randint(2,40); rst=random.randint(0,12); avg=random.randint(900,1800)
    b=int(packets*avg*random.uniform(.85,1.15))
    return {'flow_id':f'FLOW-{i:06d}','timestamp':timestamp.isoformat(),'source_ip':src,'destination_ip':dst,'source_port':random.randint(1024,65535),'destination_port':dport,'protocol':proto,'packet_count':packets,'byte_count':b,'duration_seconds':round(duration,3),'connection_count':connections,'failed_connection_count':failed,'syn_count':syn,'rst_count':rst,'average_packet_size':round(b/max(packets,1),2),'label':'NORMAL' if scenario.startswith('NORMAL_') else 'SUSPICIOUS','scenario_type':scenario}
def generate(count=5000):
    out=Path(__file__).resolve().parents[1]/'data'/'network_traffic.csv'; out.parent.mkdir(exist_ok=True)
    pd.DataFrame([make_flow(i+1) for i in range(count)]).sort_values('timestamp').to_csv(out,index=False); print(f'Generated {count} flows -> {out}')
if __name__=='__main__': generate()
