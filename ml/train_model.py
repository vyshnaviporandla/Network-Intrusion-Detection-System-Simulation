from pathlib import Path
import joblib,pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
FEATURES=['packet_count','byte_count','duration_seconds','connection_count','failed_connection_count','syn_count','rst_count','average_packet_size']
def train():
    root=Path(__file__).resolve().parents[1]; df=pd.read_csv(root/'data'/'network_traffic.csv'); X=df[FEATURES].fillna(0); y=(df.label!='NORMAL').astype(int); a,b,c,d=train_test_split(X,y,test_size=.2,random_state=42,stratify=y); model=RandomForestClassifier(n_estimators=120,random_state=42,class_weight='balanced'); model.fit(a,c); p=model.predict(b); metrics={'accuracy':round(accuracy_score(d,p),4),'precision':round(precision_score(d,p,zero_division=0),4),'recall':round(recall_score(d,p,zero_division=0),4),'f1':round(f1_score(d,p,zero_division=0),4)}; (root/'models').mkdir(exist_ok=True); joblib.dump({'model':model,'features':FEATURES,'metrics':metrics},root/'models'/'ids_random_forest.joblib'); print(metrics)
if __name__=='__main__': train()
