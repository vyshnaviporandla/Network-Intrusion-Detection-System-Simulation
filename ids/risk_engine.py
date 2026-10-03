def calculate_risk(rule_matches, anomaly_score, ml_score=None):
    """
    Calculate IDS risk score and classification.

    Classification:
    0-20   NORMAL
    21-40  LOW RISK
    41-60  SUSPICIOUS
    61-80  HIGH RISK
    81-100 CRITICAL INVESTIGATION
    """

    anomaly_score = float(anomaly_score or 0)

    # When only anomaly detection is available,
    # the anomaly score itself represents the risk.
    if not rule_matches and ml_score is None:
        risk_score = anomaly_score

    else:
        # Convert rule matches into a 0-100 rule risk.
        rule_score = min(len(rule_matches) * 20, 100)

        if ml_score is not None:
            ml_score = float(ml_score)

            # Hybrid IDS: 40% rules + 30% anomaly + 30% ML
            risk_score = (
                rule_score * 0.40
                + anomaly_score * 0.30
                + ml_score * 0.30
            )
        else:
            # IDS without ML: 60% rules + 40% anomaly
            risk_score = (
                rule_score * 0.60
                + anomaly_score * 0.40
            )

    risk_score = max(0, min(100, round(risk_score, 2)))

    if risk_score <= 20:
        classification = "NORMAL"
    elif risk_score <= 40:
        classification = "LOW RISK"
    elif risk_score <= 60:
        classification = "SUSPICIOUS"
    elif risk_score <= 80:
        classification = "HIGH RISK"
    else:
        classification = "CRITICAL INVESTIGATION"

    return risk_score, classification