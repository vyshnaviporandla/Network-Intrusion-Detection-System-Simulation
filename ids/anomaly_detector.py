import numpy as np
BASELINE={'bytes_per_second':(900000,700000),'packets_per_second':(250,220),'connection_rate':(8,12),'failure_ratio':(.08,.15),'syn_ratio':(.10,.15)}
def calculate_anomaly_score(f):
    scores=[]
    for k,(mean,std) in BASELINE.items(): scores.append(min(abs(float(f.get(k,0))-mean)/max(std,.001)/5*100,100))
    return round(float(np.mean(scores)),2)
