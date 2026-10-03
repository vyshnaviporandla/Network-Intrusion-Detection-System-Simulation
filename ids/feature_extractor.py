def n(v,d=0):
    try: x=float(v); return x if x>=0 else d
    except: return d
def extract_network_features(f):
    p=n(f.get('packet_count')); b=n(f.get('byte_count')); dur=max(n(f.get('duration_seconds')),0.001); c=n(f.get('connection_count')); fail=n(f.get('failed_connection_count')); syn=n(f.get('syn_count')); rst=n(f.get('rst_count'))
    try: port=int(f.get('destination_port',0)); port=port if 0<=port<=65535 else 0
    except: port=0
    proto=str(f.get('protocol','UNKNOWN')).upper(); proto=proto if proto in {'TCP','UDP','ICMP'} else 'UNKNOWN'
    return {'packet_count':p,'byte_count':b,'duration':dur,'bytes_per_second':b/dur,'packets_per_second':p/dur,'average_packet_size':n(f.get('average_packet_size')) or b/max(p,1),'connection_count':c,'failed_connection_count':fail,'failure_ratio':fail/max(c,1),'syn_count':syn,'rst_count':rst,'syn_ratio':syn/max(p,1),'unique_destination_ports':1,'unique_destination_ips':1,'connection_rate':c/dur,'destination_port':port,'protocol':proto}
