# Network Intrusion Detection System (IDS) Simulation

A defensive cybersecurity project that simulates network traffic, detects suspicious behavior using rule-based and anomaly-based techniques, applies optional machine learning, calculates risk scores, generates security alerts, and presents the results through a SOC-style dashboard.

> **Defensive Cybersecurity Project:** This project uses synthetic network-flow data only. It does not scan, attack, probe, exploit, or disrupt external systems.

---

## 📌 Overview

The **Network Intrusion Detection System (IDS) Simulation** is an educational cybersecurity platform designed to demonstrate how an IDS can monitor network-flow information and identify potentially suspicious behavior.

The system follows this pipeline:

```text
Synthetic Network Traffic
          ↓
    Feature Extraction
          ↓
 ┌──────────────────────┐
 │ Rule-Based Detection │
 │ Anomaly Detection    │
 │ ML Detection         │
 └──────────────────────┘
          ↓
      Risk Engine
          ↓
     Alert Engine
          ↓
      SQLite Database
          ↓
      SOC Dashboard
          ↓
 Analyst Investigation
```

The project intentionally focuses on **detection and investigation rather than prevention**.

---

## 🎯 Problem Statement

Modern networks generate large volumes of traffic that can make manual security monitoring difficult.

Security teams need mechanisms that can:

* Monitor network activity
* Extract useful security features
* Identify abnormal behavior
* Detect known suspicious patterns
* Assign risk levels
* Generate actionable alerts
* Support analyst investigation
* Provide security analytics

This project demonstrates these concepts in a safe, isolated environment using synthetic network-flow data.

---

## 🎯 Objectives

The main objectives are:

1. Generate realistic synthetic network-flow records.
2. Create a dataset containing at least 5,000 flow records.
3. Extract network-security features.
4. Implement signature/rule-based detection.
5. Implement statistical anomaly detection.
6. Integrate optional machine-learning detection.
7. Combine detection signals into a risk score.
8. Generate security alerts.
9. Store network events and alerts in SQLite.
10. Provide a SOC-style monitoring dashboard.
11. Support alert investigation and status management.
12. Provide automated tests.
13. Document the architecture and cybersecurity concepts.

---

## 🛡️ Cybersecurity Scope

This project is strictly defensive.

### The project DOES:

* Generate synthetic network traffic data.
* Simulate suspicious network behavior as data.
* Analyze network-flow characteristics.
* Detect suspicious patterns.
* Calculate anomaly scores.
* Generate security alerts.
* Support analyst investigation.
* Demonstrate SOC workflows.
* Demonstrate machine-learning classification.

### The project DOES NOT:

* Scan public networks.
* Scan third-party systems.
* Exploit vulnerabilities.
* Perform penetration testing.
* Launch denial-of-service attacks.
* Send malicious packets.
* Perform unauthorized monitoring.
* Attack external systems.

All suspicious behavior is represented as **synthetic data**.

---

# 🏗️ Architecture

```text
                   ┌───────────────────────┐
                   │ Synthetic Traffic     │
                   │ Generator             │
                   └───────────┬───────────┘
                               │
                               ▼
                   ┌───────────────────────┐
                   │ Network Flow Records  │
                   └───────────┬───────────┘
                               │
                               ▼
                   ┌───────────────────────┐
                   │ Feature Extraction    │
                   └───────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
      │ Rule Engine │  │  Anomaly     │  │ ML Detector │
      │             │  │  Detector    │  │             │
      └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                   ┌───────────────────────┐
                   │ Risk Engine           │
                   └───────────┬───────────┘
                               │
                               ▼
                   ┌───────────────────────┐
                   │ Alert Engine          │
                   └───────────┬───────────┘
                               │
                               ▼
                   ┌───────────────────────┐
                   │ SQLite Security DB    │
                   └───────────┬───────────┘
                               │
                               ▼
                   ┌───────────────────────┐
                   │ SOC Dashboard         │
                   └───────────┬───────────┘
                               │
                               ▼
                   ┌───────────────────────┐
                   │ Analyst Investigation │
                   └───────────────────────┘
```

---

# 🧰 Technology Stack

## Backend

* Python
* Flask
* Flask-CORS
* SQLite
* Pandas
* NumPy

## Machine Learning

* Scikit-learn
* Random Forest
* Joblib

## Frontend

* React
* Vite
* JavaScript
* CSS

## Testing

* Pytest

## Development

* Git
* GitHub
* Windows Command Prompt
* Python Virtual Environment

---

# 📁 Project Structure

```text
Network-IDS-Simulation/
│
├── backend/
│   ├── app.py
│   ├── seed_database.py
│   └── __init__.py
│
├── data/
│   └── network_traffic.csv
│
├── docs/
│   └── architecture.md
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx
│       └── styles.css
│
├── ids/
│   ├── alert_engine.py
│   ├── anomaly_detector.py
│   ├── correlation.py
│   ├── feature_extractor.py
│   ├── risk_engine.py
│   ├── rule_engine.py
│   └── __init__.py
│
├── ml/
│   ├── train_model.py
│   ├── predict.py
│   ├── evaluate.py
│   └── __init__.py
│
├── reports/
│   ├── project_report.md
│   └── interview_questions.md
│
├── simulator/
│   ├── generate_dataset.py
│   ├── traffic_simulator.py
│   └── __init__.py
│
├── tests/
│   ├── test_ids.py
│   └── __init__.py
│
├── screenshots/
│
├── models/
│
├── requirements.txt
├── RUN_PROJECT.bat
├── .env.example
├── .gitignore
└── README.md
```

---

# 📊 Synthetic Dataset

The project generates synthetic network-flow data instead of collecting real network packets.

The generated dataset contains:

**5,000 network-flow records**

The dataset includes fields such as:

```text
flow_id
timestamp
source_ip
destination_ip
source_port
destination_port
protocol
packet_count
byte_count
duration_seconds
connection_count
failed_connection_count
syn_count
rst_count
average_packet_size
label
scenario_type
```

Reserved documentation IP ranges are used for synthetic traffic representation:

```text
192.0.2.0/24
198.51.100.0/24
203.0.113.0/24
```

---

# 🧪 Traffic Scenarios

The generator supports normal and suspicious synthetic scenarios.

### Normal scenarios

```text
NORMAL_WEB
NORMAL_DNS
NORMAL_SSH
NORMAL_EMAIL
NORMAL_DATABASE
```

### Suspicious scenarios

```text
HIGH_CONNECTION_RATE
REPEATED_FAILED_CONNECTIONS
MULTI_PORT_PROBING_PATTERN
SYN_HEAVY_PATTERN
UNUSUAL_PORT_ACTIVITY
HIGH_TRAFFIC_VOLUME
```

These scenarios represent **data patterns**, not actual attacks.

---

# 🔎 Feature Engineering

The feature extraction module derives security-relevant characteristics from network flows.

Important features include:

```text
packet_count
byte_count
duration
bytes_per_second
packets_per_second
average_packet_size
connection_count
failed_connection_count
failure_ratio
syn_count
rst_count
syn_ratio
unique_destination_ports
unique_destination_ips
connection_rate
```

These features allow the IDS to reason about:

* Traffic volume
* Connection frequency
* Failed connections
* SYN activity
* Destination diversity
* Packet rates
* Byte rates
* Behavioral deviations

---

# 🚨 Signature-Based Detection

The rule engine identifies predefined suspicious patterns.

Examples include:

### High Connection Rate

Detects unusually high connection activity.

### Repeated Failed Connections

Detects excessive failed connection attempts.

### Multiple Destination Ports

Detects unusually broad destination-port activity.

### SYN-Heavy Behavior

Detects unusually high SYN activity.

### Unusual Service-Port Activity

Detects unexpected activity involving service ports.

### High Traffic Volume

Detects abnormally large traffic volumes.

A rule match indicates **suspicious behavior requiring investigation**. It does not automatically prove malicious activity.

---

# 📈 Anomaly Detection

The project includes statistical anomaly analysis.

The anomaly detector produces an:

```text
Anomaly Score: 0–100
```

Higher values indicate greater deviation from the expected behavior represented by the project's baseline.

Anomaly detection is useful for identifying unusual patterns that may not match predefined signatures.

However, anomaly detection can generate false positives because unusual legitimate behavior may also deviate from the baseline.

---

# 🤖 Machine Learning

The project includes an optional machine-learning component.

The implemented model uses:

```text
Random Forest
```

The training process uses the generated synthetic dataset.

The project also includes ML prediction and evaluation modules.

Evaluation concepts include:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

## Important Evaluation Note

The generated dataset is synthetic and contains clearly defined scenarios. Therefore, machine-learning performance on this dataset should **not** be interpreted as equivalent to performance on real enterprise network traffic.

The model's reported results are valid for the generated experimental dataset only.

---

# 🔀 Hybrid Detection

The project combines multiple detection approaches:

```text
Signature Detection
        +
Anomaly Detection
        +
Optional ML Detection
        =
Hybrid IDS
```

The goal is to demonstrate how different detection signals can contribute to security analysis.

When ML is unavailable, the risk engine can operate using rule-based and anomaly signals.

---

# ⚠️ Risk Scoring

The system produces a risk score between:

```text
0–100
```

The project's classification thresholds are:

| Risk Score | Classification         |
| ---------: | ---------------------- |
|       0–20 | NORMAL                 |
|      21–40 | LOW RISK               |
|      41–60 | SUSPICIOUS             |
|      61–80 | HIGH RISK              |
|     81–100 | CRITICAL INVESTIGATION |

These thresholds are project-defined assumptions used for demonstration and can be tuned for different environments.

---

# 🚨 Security Alerts

Detected suspicious behavior is converted into security alerts.

Alerts contain information such as:

```text
Alert ID
Timestamp
Source IP
Destination IP
Protocol
Source Port
Destination Port
Rule ID
Alert Type
Severity
Risk Score
Description
Status
```

Alert statuses include:

```text
NEW
INVESTIGATING
RESOLVED
FALSE_POSITIVE
```

---

# 👨‍💻 SOC Investigation Workflow

The project demonstrates a simplified SOC workflow:

```text
Network Event
      ↓
IDS Detection
      ↓
Alert
      ↓
SOC Queue
      ↓
Triage
      ↓
Investigation
      ↓
Determine Severity
      ↓
Resolve / Escalate / False Positive
      ↓
Document
```

Analysts can inspect alert details and update the investigation status.

---

# 🖥️ SOC Dashboard

The React dashboard provides a security-monitoring view containing:

### Dashboard Metrics

* Total Network Flows
* Normal Traffic
* Suspicious Traffic
* Open Alerts
* Critical Alerts
* Average Risk Score

### Analytics

* Traffic over time
* Normal vs suspicious traffic
* Top alert types

### Alert Management

* Recent alerts
* Alert details
* Source and destination information
* Ports and protocol
* Rule information
* Severity
* Risk score
* Investigation status

The dashboard polls the backend API for updated information.

---

# 🔌 REST API

The backend exposes REST-style endpoints for IDS data and dashboard operations.

## Network Flows

```http
POST /api/flows
GET /api/flows
GET /api/flows/{id}
```

## Alerts

```http
GET /api/alerts
GET /api/alerts/{id}
PUT /api/alerts/{id}/status
POST /api/alerts/{id}/notes
```

## Dashboard

```http
GET /api/dashboard/stats
GET /api/dashboard/traffic
GET /api/dashboard/alerts
```

## Rules

```http
GET /api/rules
```

---

# 🗄️ Database

The project uses SQLite for local storage.

The database is generated as:

```text
data/ids.db
```

It stores network-flow and alert information used by the backend and dashboard.

SQLite was selected because it provides a lightweight database suitable for a beginner-friendly local cybersecurity demonstration.

---

# ⚙️ Installation

## 1. Clone the repository

```cmd
git clone https://github.com/vyshnaviporandla/Network-Intrusion-Detection-System-Simulation.git
```

```cmd
cd Network-Intrusion-Detection-System-Simulation
```

---

## 2. Create a Python virtual environment

```cmd
python -m venv venv
```

---

## 3. Activate the environment

Windows:

```cmd
venv\Scripts\activate
```

---

## 4. Install Python dependencies

```cmd
pip install -r requirements.txt
```

---

## 5. Install frontend dependencies

```cmd
cd frontend
npm install
cd ..
```

---

# ▶️ Running the Project

## Generate the dataset

From the project root:

```cmd
python simulator\generate_dataset.py
```

This generates:

```text
data\network_traffic.csv
```

---

## Train the machine-learning model

```cmd
python ml\train_model.py
```

The trained model is stored under:

```text
models/
```

---

## Seed the database

```cmd
python backend\seed_database.py
```

The seed process loads the synthetic network traffic and processes it through the IDS pipeline.

Example project result:

```text
Flows processed : 5000
Alerts generated: 2741
Database        : data\ids.db
```

---

# 🚀 Start the Backend

From the project root:

```cmd
python backend\app.py
```

The Flask backend runs locally at:

```text
http://127.0.0.1:5000
```

---

# 🌐 Start the Frontend

Open another Command Prompt.

Navigate to:

```cmd
cd frontend
```

Run:

```cmd
npm run dev
```

Vite will provide the local frontend address.

Open that address in your browser.

---

# 🧪 Testing

The project includes automated tests using Pytest.

Run:

```cmd
python -m pytest -q
```

The implemented test suite covers core IDS functionality including:

* Feature extraction
* Rule detection
* Anomaly scoring
* Risk scoring
* IDS-related processing

Current project validation:

```text
5 passed
```

---

# 📊 Project Results

The current implementation successfully generated and processed:

| Metric                    |   Result |
| ------------------------- | -------: |
| Synthetic network flows   |    5,000 |
| Generated security alerts |    2,741 |
| Automated tests           | 5 passed |
| Backend                   |  Working |
| Frontend dashboard        |  Working |
| Alert investigation       |  Working |
| Alert status management   |  Working |
| ML model                  |  Trained |

The alerts are generated from synthetic scenarios and therefore represent a controlled educational experiment rather than production security telemetry.

---

# 🔬 False Positives and False Negatives

## False Positive

A legitimate event is incorrectly classified as suspicious.

Example:

```text
A legitimate backup operation produces unusually high network traffic.
```

The IDS may interpret the traffic as suspicious because it exceeds a configured threshold.

## False Negative

Suspicious behavior is classified as normal.

False negatives are important because an IDS can miss activity that does not match its rules or baseline.

Potential improvements include:

* Better behavioral baselines
* Threshold tuning
* Multiple detection methods
* Contextual information
* Analyst feedback
* Improved machine-learning models
* Larger and more representative datasets

---

# 🧠 IDS vs IPS

## IDS

An Intrusion Detection System:

```text
Detects → Analyzes → Alerts
```

It primarily focuses on identifying potentially suspicious activity.

## IPS

An Intrusion Prevention System can additionally take preventive action against detected activity.

This project intentionally implements an **IDS simulation** and does not automatically block or disrupt network traffic.

---

# 🔍 Signature vs Anomaly Detection

| Feature            | Signature-Based                | Anomaly-Based               |
| ------------------ | ------------------------------ | --------------------------- |
| Detection approach | Known patterns                 | Behavioral deviations       |
| Explainability     | High                           | Moderate                    |
| Unknown patterns   | May miss them                  | Can potentially detect them |
| False positives    | Can be lower for precise rules | Can be higher               |
| Main strength      | Known suspicious behavior      | Unusual behavior            |

The project combines these approaches to demonstrate hybrid security monitoring.

---

# 🧩 Event vs Alert vs Incident

### Event

An observed network activity record.

```text
Example:
A connection between two synthetic IP addresses.
```

### Alert

An event that crosses a detection rule or risk threshold and requires investigation.

### Incident

A confirmed or sufficiently investigated security event requiring incident-management action.

A rule match alone does not automatically prove that an event is a confirmed incident.

---

# 🛡️ Security and Privacy

The project follows defensive-security principles.

Important considerations for production systems include:

* Authentication
* Authorization
* Least privilege
* HTTPS
* Secure API configuration
* Environment-based secrets
* Log protection
* Input validation
* API rate limiting
* Audit logging
* Protection of analyst notes
* Avoiding unnecessary packet-payload storage

Network-security telemetry can itself contain sensitive information, so access to IDS data should be controlled.

---

# ⚠️ Limitations

This project is an educational IDS simulation and has several limitations.

### Synthetic Data

The dataset does not represent the full complexity of real enterprise networks.

### Simplified Detection

The detection rules use predefined thresholds.

### Limited Baseline

The anomaly detector uses a simplified baseline rather than a continuously learned enterprise baseline.

### ML Dataset

The machine-learning model is trained on synthetic data.

### Local Deployment

The current implementation is designed for local demonstration.

### No Automated Prevention

The system detects and reports suspicious activity but does not automatically block traffic.

### Limited Authentication

The current educational dashboard does not implement a complete production-grade SOC authentication system.

---

# 🔮 Future Improvements

Possible defensive improvements include:

* Authorized PCAP ingestion
* Real-time flow ingestion
* Zeek integration
* Suricata integration
* SIEM integration
* Threat-intelligence enrichment
* Improved anomaly models
* Behavioral baselines
* Advanced alert correlation
* Detection-rule tuning
* User/entity behavior analytics
* Cloud IDS monitoring
* Container deployment
* Centralized logging
* Model-drift monitoring
* Production authentication and authorization

---

# 🧩 MITRE ATT&CK Considerations

Network-security alerts can potentially be mapped to the MITRE ATT&CK framework when sufficient evidence exists.

However:

> A statistical anomaly does not automatically prove a specific ATT&CK technique.

ATT&CK mapping should be based on supporting evidence and can help with:

* Detection documentation
* SOC investigation
* Threat hunting
* Security reporting

This project keeps ATT&CK interpretation at a high level because its traffic is synthetic.

---

# 📡 SIEM Integration Concept

In a production environment, IDS alerts could be forwarded to a Security Information and Event Management system.

A possible architecture would be:

```text
Network Traffic
      ↓
IDS
      ↓
Security Alerts
      ↓
SIEM
      ↓
Correlation
      ↓
SOC Analyst
      ↓
Investigation / Response
```

The current project demonstrates the IDS and SOC-analysis concepts locally without requiring a commercial SIEM platform.

---

# 📸 Recommended Screenshots

For project documentation, capture:

```text
01-project-structure.png
02-architecture.png
03-synthetic-dataset.png
04-traffic-simulation.png
05-feature-extraction.png
06-rule-detection.png
07-anomaly-score.png
08-risk-score.png
09-alert-generated.png
10-soc-dashboard.png
11-traffic-chart.png
12-alert-investigation.png
13-alert-status.png
14-database-records.png
15-ml-evaluation.png
16-confusion-matrix.png
17-automated-tests.png
18-api-response.png
19-github-repository.png
20-readme-preview.png
```

---

# 📚 Learning Outcomes

Through this project, the following concepts were practiced:

* Network security fundamentals
* Intrusion Detection Systems
* Network-flow analysis
* Feature engineering
* Signature-based detection
* Anomaly detection
* Risk scoring
* Security alert generation
* Alert investigation
* SOC workflows
* Machine learning
* Classification metrics
* SQLite database design
* REST API development
* React dashboard development
* Automated testing
* Git and GitHub
* Defensive cybersecurity practices

---

# 💼 Project Highlights

### Technical Highlights

```text
Python
Flask
React
SQLite
Pandas
NumPy
Scikit-learn
Random Forest
Pytest
REST API
Git/GitHub
```

### Cybersecurity Highlights

```text
Network Traffic Analysis
Intrusion Detection
Signature Detection
Anomaly Detection
Security Alerts
Risk Scoring
SOC Workflow
Incident Investigation
Security Analytics
```

---

# 🎓 Educational Use

This project is intended for:

* Cybersecurity students
* Network-security learners
* SOC analyst preparation
* Python practice
* Machine-learning experimentation
* Academic project demonstrations
* Defensive cybersecurity portfolios

---

# ⚖️ Ethical Disclaimer

This project is designed exclusively for defensive cybersecurity education.

All suspicious network behavior is represented using synthetic data or authorized isolated lab environments.

Do not use this project to scan, probe, attack, exploit, or disrupt systems that you do not own or have explicit authorization to test.

---

# 👤 Author

**Vyshnavi Porandla**

Cybersecurity • Network Security • Python • Machine Learning • Security Analytics

GitHub:

https://github.com/vyshnaviporandla

---

# ⭐ Project Repository

**Network Intrusion Detection System Simulation**

GitHub repository:

https://github.com/vyshnaviporandla/Network-Intrusion-Detection-System-Simulation

---

# 📌 Project Status

```text
Project Type: Academic / Defensive Cybersecurity
Status: Completed Core Implementation
Dataset: Synthetic
Flows: 5,000
Alerts: 2,741
Automated Tests: 5 passed
Backend: Flask
Frontend: React + Vite
Database: SQLite
ML: Random Forest
```

---

## 🚀 Final Summary

The **Network Intrusion Detection System (IDS) Simulation** demonstrates an end-to-end defensive security workflow:

```text
Generate
   ↓
Analyze
   ↓
Detect
   ↓
Score
   ↓
Alert
   ↓
Investigate
   ↓
Document
```

The project provides a practical demonstration of how network-flow monitoring, rule-based detection, anomaly detection, machine learning, risk scoring, alert management, and SOC-style investigation can work together in a controlled cybersecurity environment.
