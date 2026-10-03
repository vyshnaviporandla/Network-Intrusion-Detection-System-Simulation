# Architecture
Synthetic Traffic Generator -> Flow Collector -> Feature Extractor -> Signature Rules + Statistical Anomaly Detection + Optional Random Forest -> Risk Engine -> Alert Engine -> SQLite -> SOC Dashboard.

All traffic is synthetic. No packets are transmitted.
