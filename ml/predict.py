from pathlib import Path
import joblib,pandas as pd
def predict_ml(flow):
    p=Path(__file__).resolve().parents[1]/'models'/'ids_random_forest.joblib'
    if not p.exists(): return None
    x=joblib.load(p); X=pd.DataFrame([{f:float(flow.get(f,0) or 0) for f in x['features']}]); return round(float(x['model'].predict_proba(X)[0][1]*100),2)
