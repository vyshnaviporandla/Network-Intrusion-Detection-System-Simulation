import time,random
from .generate_dataset import make_flow
def stream(mode='mixed',speed='slow'):
    delay=2 if speed=='slow' else .4; i=1
    while True:
        scenario=random.choice(['NORMAL_WEB','NORMAL_DNS','NORMAL_SSH','NORMAL_EMAIL','NORMAL_DATABASE']) if mode=='normal' else None
        yield make_flow(900000+i,scenario); i+=1; time.sleep(delay)
