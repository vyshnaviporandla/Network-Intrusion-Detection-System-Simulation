# 🛡️ Network Intrusion Detection System (IDS) Simulation

A defensive cybersecurity project that simulates a **Network Intrusion Detection System (IDS)** using synthetic network traffic.

The system analyzes network-flow records using **rule/signature detection, anomaly detection, machine learning, and risk scoring**, generates security alerts, stores results in SQLite, and presents them through a **React-based SOC dashboard**.

> **Educational / Defensive Project:** This project uses synthetic network traffic only. It does not perform real-world scanning, exploitation, probing, DDoS attacks, or interaction with third-party systems.

---

## 🚀 Live Demo

### Frontend — SOC Dashboard

https://network-ids-dashboard.onrender.com/

### Backend API

https://network-intrusion-detection-system-wgn8.onrender.com/

### Dashboard Statistics API

https://network-intrusion-detection-system-wgn8.onrender.com/api/dashboard/stats

---

## 📌 Project Overview

Traditional network monitoring can generate large amounts of traffic information that security analysts need to interpret.

This project demonstrates a simplified SOC-style detection pipeline:

```text
Synthetic Network Traffic
          ↓
Feature Extraction
          ↓
Rule / Signature Detection
          ↓
Anomaly Detection
          ↓
Machine Learning
          ↓
Risk Scoring
          ↓
Security Alerts
          ↓
SQLite Database
          ↓
Flask REST API
          ↓
React SOC Dashboard
```

The dashboard allows users to monitor traffic statistics, suspicious activity, alert types, risk scores, and recent security alerts.

---

## 🎯 Objectives

* Generate synthetic network-flow data.
* Process and extract useful network features.
* Detect suspicious traffic using predefined rules.
* Calculate anomaly scores.
* Integrate a machine-learning detection component.
* Calculate a 0–100 risk score.
* Generate and store security alerts.
* Provide APIs for dashboard data.
* Build a SOC-style monitoring dashboard.
* Deploy the application using GitHub and Render.
* Demonstrate defensive cybersecurity concepts safely.

---

## 🧰 Technology Stack

| Component            | Technology    |
| -------------------- | ------------- |
| Programming Language | Python        |
| Backend              | Flask         |
| Frontend             | React         |
| Build Tool           | Vite          |
| Database             | SQLite        |
| Data Processing      | Pandas, NumPy |
| Machine Learning     | Scikit-learn  |
| Model Storage        | Joblib        |
| Testing              | Pytest        |
| Version Control      | Git / GitHub  |
| Deployment           | Render        |

---

## 📂 Project Structure

```text
Network-IDS-Simulation/
│
├── backend/
│   ├── app.py
│   ├── seed_database.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── package.json
│   └── vite.config.js
│
├── ids/
│   ├── feature_extractor.py
│   ├── rule_engine.py
│   ├── anomaly_detector.py
│   ├── risk_engine.py
│   └── alert_engine.py
│
├── ml/
│   └── predict.py
│
├── simulator/
│   └── traffic_simulator.py
│
├── data/
│   ├── network_traffic.csv
│   └── ids.db
│
├── models/
│   └── ids_random_forest.joblib
│
├── tests/
│
├── screenshots/
│
├── docs/
│
├── reports/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🔍 Detection Pipeline

### 1. Synthetic Traffic

The project uses generated network-flow records instead of real network traffic.

The dataset contains:

```text
5,000 synthetic network-flow records
```

This allows the project to demonstrate detection concepts without interacting with real systems.

---

### 2. Feature Extraction

Network-flow information is transformed into features that can be evaluated by the IDS components.

Examples include traffic volume, connection behavior, ports, and other flow-level characteristics.

---

### 3. Rule-Based Detection

The rule engine identifies predefined suspicious patterns.

Examples observed in the dashboard include:

* Repeated failed connections
* Excessive connection rate
* High destination port/connection activity
* High traffic volume

---

### 4. Anomaly Detection

The anomaly component calculates a statistical anomaly score to identify traffic that differs from expected behavior.

The anomaly score contributes to the overall risk assessment.

---

### 5. Machine Learning

A Random Forest model is integrated into the detection pipeline.

The trained model is stored using Joblib:

```text
models/ids_random_forest.joblib
```

The machine-learning component provides an additional detection signal alongside the rule and anomaly components.

> **Important:** The recorded ML evaluation produced 1.00 accuracy, precision, recall, and F1 on the synthetic dataset. These values should not be interpreted as real-world IDS performance because the dataset is synthetic and controlled for demonstration.

---

## ⚠️ Risk Classification

The IDS converts detection signals into a risk score from:

```text
0 – 100
```

The implemented classification ranges are:

| Risk Score | Classification         |
| ---------: | ---------------------- |
|       0–20 | NORMAL                 |
|      21–40 | LOW RISK               |
|      41–60 | SUSPICIOUS             |
|      61–80 | HIGH RISK              |
|     81–100 | CRITICAL INVESTIGATION |

---

## 🚨 Alert System

Detected suspicious activity is converted into security alerts.

Each alert can contain information such as:

* Timestamp
* Source IP
* Destination
* Alert type
* Severity
* Risk score
* Status

The dashboard supports investigation-oriented alert statuses such as:

```text
NEW
↓
INVESTIGATING
↓
RESOLVED
```

---

## 📊 Live Deployment Results

The deployed dashboard currently reports:

| Metric              | Value |
| ------------------- | ----: |
| Total Network Flows | 5,000 |
| Normal Traffic      | 2,199 |
| Suspicious Traffic  | 2,801 |
| Open Alerts         | 2,936 |
| Critical Alerts     |     1 |
| Average Risk Score  | 29.52 |

Traffic distribution:

```text
Normal      44%
Suspicious  56%
```

---

## 📈 Dashboard Features

The React SOC dashboard provides:

* Backend connection status
* Total network-flow count
* Normal traffic statistics
* Suspicious traffic statistics
* Open-alert count
* Critical-alert count
* Average risk score
* Traffic-over-time visualization
* Traffic classification
* Top alert types
* Recent security alerts
* Alert severity
* Alert risk scores
* Alert investigation status

---

## 🔌 API

The Flask backend exposes API endpoints used by the dashboard.

### Dashboard Statistics

```http
GET /api/dashboard/stats
```

Example:

```json
{
  "average_risk_score": 29.52,
  "critical_alerts": 1,
  "normal_traffic": 2199,
  "open_alerts": 2936,
  "suspicious_traffic": 2801,
  "total_flows": 5000
}
```

### Alerts

```http
GET /api/alerts
```

### Traffic Data

```http
GET /api/dashboard/traffic
```

Alert status operations are also provided by the backend for the investigation workflow.

---

## 💻 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/vyshnaviporandla/Network-Intrusion-Detection-System-Simulation.git
```

```bash
cd Network-Intrusion-Detection-System-Simulation
```

---

### 2. Create a Python virtual environment

Windows:

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

---

### 3. Install Python dependencies

```cmd
pip install -r requirements.txt
```

---

### 4. Seed the database

```cmd
cd backend
python seed_database.py
```

The database is created under:

```text
data/ids.db
```

---

### 5. Start the Flask backend

```cmd
python app.py
```

The local backend runs at:

```text
http://127.0.0.1:5000
```

---

### 6. Start the React frontend

Open another Command Prompt:

```cmd
cd frontend
npm install
npm run dev
```

Vite will provide the local development URL.

---

## 🧪 Testing

The project includes an automated Pytest suite covering core IDS behavior.

Run:

```cmd
pytest
```

Current implementation:

```text
5 tests passing
```

---

## ☁️ Deployment

The application is deployed using Render.

### Backend

The backend is deployed as a Web Service.

Configuration:

```text
Root Directory:
backend/

Build Command:
pip install -r ../requirements.txt

Start Command:
python seed_database.py && gunicorn app:app
```

### Frontend

The React application is deployed as a Static Site.

Configuration:

```text
Root Directory:
frontend/

Build Command:
npm install && npm run build

Publish Directory:
dist
```

---

## 🔐 Security & Ethical Scope

This project follows a defensive cybersecurity approach.

### The project DOES:

* Generate synthetic network traffic.
* Analyze simulated traffic.
* Detect simulated suspicious patterns.
* Generate simulated security alerts.
* Demonstrate SOC monitoring concepts.
* Use safe documentation/test IP ranges.

### The project DOES NOT:

* Scan real networks.
* Perform exploitation.
* Perform unauthorized access.
* Launch DDoS attacks.
* Probe third-party systems.
* Collect real users' network traffic.
* Deploy malware.
* Provide offensive attack automation.

---

## 🧠 Key Cybersecurity Concepts Demonstrated

### Observation

A network-flow record representing observed traffic information.

### Indicator

A feature or behavior that may provide evidence of suspicious activity.

### Alert

A generated notification requiring analyst attention.

### Threat

A potential malicious or harmful condition represented within the simulation.

### Incident

An event requiring investigation or response.

### Risk

A numerical representation of the potential security significance of detected behavior.

### Confidence

How strongly the implemented detection signals support a detection conclusion.

---

## ⚠️ Current Limitations

This is an educational IDS simulation rather than a production enterprise IDS.

Current limitations include:

* Synthetic data rather than live network telemetry.
* Simplified anomaly detection.
* Simplified machine-learning feature set.
* SQLite used for the demonstration database.
* Five automated tests in the current implementation.
* Simplified SOC dashboard.
* No MITRE ATT&CK mapping in the current application.
* No SIEM integration.
* No production-scale distributed processing.
* Cloud SQLite data is suitable for demonstration but is not a substitute for production persistent database architecture.

---

## 🔮 Future Improvements

Potential future development includes:

* Larger and more diverse synthetic datasets.
* More sophisticated anomaly detection.
* Additional ML models.
* Model evaluation using independent test data.
* Explainable ML results.
* MITRE ATT&CK technique mapping.
* Advanced incident-management workflows.
* More dashboard filters and visualizations.
* Production database integration.
* SIEM integration.
* Authentication and role-based access control.
* Persistent cloud storage.
* Expanded automated testing.
* Containerized deployment.

---

## 📚 Learning Outcomes

This project provided practical experience with:

* Network security monitoring
* IDS architecture
* Rule-based detection
* Anomaly detection
* Machine learning for cybersecurity
* Risk scoring
* Alert generation
* Flask REST APIs
* React dashboards
* SQLite database design
* Python data processing
* Automated testing
* Git/GitHub workflows
* Cloud deployment
* SOC concepts

---

## 👩‍💻 Author

**Vyshnavi Porandla**

GitHub:

https://github.com/vyshnaviporandla

Repository:

https://github.com/vyshnaviporandla/Network-Intrusion-Detection-System-Simulation

---

## 📄 Project Status

```text
✅ Synthetic dataset generated
✅ IDS detection pipeline implemented
✅ Rule-based detection implemented
✅ Anomaly detection implemented
✅ ML component implemented
✅ Risk scoring implemented
✅ Alert system implemented
✅ SQLite database implemented
✅ REST API implemented
✅ React SOC dashboard implemented
✅ Automated tests implemented
✅ GitHub repository created
✅ Backend deployed
✅ Frontend deployed
✅ Live dashboard connected to backend
```

---

## ⚠️ Disclaimer

This project is created for **educational and defensive cybersecurity purposes**.

All network activity represented by the application is synthetic. The project should not be used to monitor, scan, attack, exploit, or interfere with systems without explicit authorization.
