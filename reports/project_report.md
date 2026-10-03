# Network Intrusion Detection System (IDS) Simulation

## Abstract
A defensive IDS simulation using synthetic network flows, rule detection, statistical anomaly detection, optional Random Forest ML, risk scoring and a SOC dashboard.

## Detection
Signature rules detect excessive connection rate, repeated failures, SYN-heavy behavior, unusual service ports and high traffic volume. Anomaly scoring compares features with a statistical baseline. The hybrid risk engine combines rule, anomaly and ML evidence.

## SOC Workflow
Observation -> Detection -> Alert -> Triage -> Investigation -> Resolution or False Positive.

## Limitations
Synthetic traffic cannot represent all production network behavior. Thresholds are project assumptions and false positives/negatives are possible.
