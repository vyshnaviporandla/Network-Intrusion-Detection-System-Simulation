import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

const API = "http://127.0.0.1:5000/api";

function StatCard({ title, value, subtitle, danger }) {
  return (
    <div className={`stat-card ${danger ? "danger" : ""}`}>
      <div className="stat-title">{title}</div>
      <div className="stat-value">{value}</div>
      <div className="stat-subtitle">{subtitle}</div>
    </div>
  );
}

function SeverityBadge({ severity }) {
  const value = severity || "INFO";

  return (
    <span className={`badge badge-${value.toLowerCase()}`}>
      {value}
    </span>
  );
}

function RiskBar({ score }) {
  const value = Number(score || 0);

  return (
    <div className="risk-wrapper">
      <div className="risk-track">
        <div
          className="risk-fill"
          style={{ width: `${Math.min(100, value)}%` }}
        />
      </div>
      <span>{value.toFixed(1)}</span>
    </div>
  );
}

function App() {
  const [stats, setStats] = useState({
    total_flows: 0,
    normal_traffic: 0,
    suspicious_traffic: 0,
    open_alerts: 0,
    critical_alerts: 0,
    average_risk_score: 0,
  });

  const [alerts, setAlerts] = useState([]);
  const [traffic, setTraffic] = useState([]);
  const [loading, setLoading] = useState(true);
  const [backendStatus, setBackendStatus] = useState("Checking...");
  const [selectedAlert, setSelectedAlert] = useState(null);

  async function loadDashboard() {
    try {
      const [statsResponse, alertsResponse, trafficResponse] =
        await Promise.all([
          fetch(`${API}/dashboard/stats`),
          fetch(`${API}/alerts`),
          fetch(`${API}/dashboard/traffic`),
        ]);

      if (!statsResponse.ok || !alertsResponse.ok || !trafficResponse.ok) {
        throw new Error("API request failed");
      }

      const statsData = await statsResponse.json();
      const alertsData = await alertsResponse.json();
      const trafficData = await trafficResponse.json();

      setStats(statsData);
      setAlerts(Array.isArray(alertsData) ? alertsData : []);
      setTraffic(Array.isArray(trafficData) ? trafficData : []);
      setBackendStatus("Connected");
    } catch (error) {
      console.error("Dashboard API error:", error);
      setBackendStatus("Backend unavailable");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadDashboard();

    const timer = setInterval(loadDashboard, 5000);

    return () => clearInterval(timer);
  }, []);

  async function updateAlertStatus(alertId, status) {
    try {
      const response = await fetch(`${API}/alerts/${alertId}/status`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ status }),
      });

      if (!response.ok) {
        throw new Error("Unable to update alert");
      }

      await loadDashboard();
      setSelectedAlert(null);
    } catch (error) {
      console.error(error);
      alert("Could not update alert status.");
    }
  }

  const normalPercentage =
    stats.total_flows > 0
      ? Math.round((stats.normal_traffic / stats.total_flows) * 100)
      : 0;

  const suspiciousPercentage =
    stats.total_flows > 0
      ? Math.round((stats.suspicious_traffic / stats.total_flows) * 100)
      : 0;

  const maxTraffic = Math.max(
    1,
    ...traffic.map((item) => Number(item.count || 0))
  );

  const alertTypeCounts = {};

  alerts.forEach((alert) => {
    const type = alert.alert_type || "Unknown";
    alertTypeCounts[type] = (alertTypeCounts[type] || 0) + 1;
  });

  const topAlertTypes = Object.entries(alertTypeCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 6);

  return (
    <div className="app">
      <header className="topbar">
        <div>
          <div className="brand">Network IDS</div>
          <div className="brand-subtitle">
            Network Intrusion Detection System Simulation
          </div>
        </div>

        <div className="connection">
          <span
            className={`status-dot ${
              backendStatus === "Connected" ? "online" : ""
            }`}
          />
          {backendStatus}
        </div>
      </header>

      <main className="container">
        <section className="hero">
          <div>
            <h1>SOC Security Dashboard</h1>
            <p>
              Monitor synthetic network traffic, detect suspicious patterns,
              investigate alerts, and review risk.
            </p>
          </div>

          <button className="refresh-button" onClick={loadDashboard}>
            Refresh
          </button>
        </section>

        <section className="stats-grid">
          <StatCard
            title="Total Network Flows"
            value={stats.total_flows}
            subtitle="Synthetic traffic records"
          />

          <StatCard
            title="Normal Traffic"
            value={`${normalPercentage}%`}
            subtitle={`${stats.normal_traffic} normal flows`}
          />

          <StatCard
            title="Suspicious Traffic"
            value={`${suspiciousPercentage}%`}
            subtitle={`${stats.suspicious_traffic} suspicious flows`}
            danger={stats.suspicious_traffic > 0}
          />

          <StatCard
            title="Open Alerts"
            value={stats.open_alerts}
            subtitle="Requires investigation"
            danger={stats.open_alerts > 0}
          />

          <StatCard
            title="Critical Alerts"
            value={stats.critical_alerts}
            subtitle="High-priority events"
            danger={stats.critical_alerts > 0}
          />

          <StatCard
            title="Average Risk"
            value={Number(stats.average_risk_score || 0).toFixed(1)}
            subtitle="Risk score 0–100"
          />
        </section>

        <section className="dashboard-grid">
          <div className="panel large">
            <div className="panel-header">
              <div>
                <h2>Traffic Over Time</h2>
                <p>Flow volume from the IDS database</p>
              </div>
            </div>

            {traffic.length === 0 ? (
              <div className="empty-state">
                <div className="empty-icon">◌</div>
                <h3>No traffic data yet</h3>
                <p>
                  Generate and load the synthetic dataset to populate this
                  chart.
                </p>
              </div>
            ) : (
              <div className="traffic-chart">
                {traffic.slice(-20).map((item, index) => {
                  const count = Number(item.count || 0);
                  const height = Math.max(8, (count / maxTraffic) * 100);

                  return (
                    <div className="traffic-column" key={index}>
                      <div
                        className="traffic-bar"
                        style={{ height: `${height}%` }}
                        title={`${count} flows`}
                      />
                      <span>{index + 1}</span>
                    </div>
                  );
                })}
              </div>
            )}
          </div>

          <div className="panel">
            <div className="panel-header">
              <div>
                <h2>Traffic Classification</h2>
                <p>Normal versus suspicious</p>
              </div>
            </div>

            <div className="classification">
              <div
                className="classification-circle"
                style={{
                  background: `conic-gradient(
                    #22c55e ${normalPercentage}%,
                    #ef4444 ${normalPercentage}% ${
                    normalPercentage + suspiciousPercentage
                  }%,
                    #334155 ${
                      normalPercentage + suspiciousPercentage
                    }% 100%
                  )`,
                }}
              >
                <div>
                  <strong>{normalPercentage}%</strong>
                  <span>Normal</span>
                </div>
              </div>

              <div className="legend">
                <div>
                  <span className="legend-dot normal" />
                  Normal
                  <strong>{stats.normal_traffic}</strong>
                </div>

                <div>
                  <span className="legend-dot suspicious" />
                  Suspicious
                  <strong>{stats.suspicious_traffic}</strong>
                </div>
              </div>
            </div>
          </div>

          <div className="panel">
            <div className="panel-header">
              <div>
                <h2>Top Alert Types</h2>
                <p>Most frequently detected patterns</p>
              </div>
            </div>

            {topAlertTypes.length === 0 ? (
              <div className="empty-small">No alerts yet</div>
            ) : (
              <div className="alert-types">
                {topAlertTypes.map(([type, count]) => (
                  <div className="alert-type-row" key={type}>
                    <span>{type}</span>
                    <div className="mini-track">
                      <div
                        className="mini-fill"
                        style={{
                          width: `${Math.min(
                            100,
                            (count / topAlertTypes[0][1]) * 100
                          )}%`,
                        }}
                      />
                    </div>
                    <strong>{count}</strong>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="panel">
            <div className="panel-header">
              <div>
                <h2>IDS Workflow</h2>
                <p>Detection pipeline</p>
              </div>
            </div>

            <div className="workflow">
              <div className="workflow-step">
                <span>1</span>
                Synthetic Traffic
              </div>
              <div className="workflow-arrow">↓</div>
              <div className="workflow-step">
                <span>2</span>
                Feature Extraction
              </div>
              <div className="workflow-arrow">↓</div>
              <div className="workflow-step">
                <span>3</span>
                Rules + Anomaly + ML
              </div>
              <div className="workflow-arrow">↓</div>
              <div className="workflow-step">
                <span>4</span>
                Risk & Alerts
              </div>
            </div>
          </div>
        </section>

        <section className="panel alerts-panel">
          <div className="panel-header">
            <div>
              <h2>Recent Security Alerts</h2>
              <p>Investigate detected suspicious network behavior</p>
            </div>

            <span className="alert-count">
              {alerts.length} alerts
            </span>
          </div>

          {loading ? (
            <div className="empty-state">
              <h3>Loading dashboard...</h3>
            </div>
          ) : alerts.length === 0 ? (
            <div className="empty-state">
              <div className="empty-icon">✓</div>
              <h3>No security alerts</h3>
              <p>
                The dashboard is running. Alerts will appear after network
                flows are processed.
              </p>
            </div>
          ) : (
            <div className="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Time</th>
                    <th>Source IP</th>
                    <th>Destination</th>
                    <th>Alert Type</th>
                    <th>Severity</th>
                    <th>Risk</th>
                    <th>Status</th>
                    <th />
                  </tr>
                </thead>

                <tbody>
                  {alerts.slice(0, 25).map((alert) => (
                    <tr key={alert.alert_id}>
                      <td>
                        {alert.timestamp
                          ? new Date(alert.timestamp).toLocaleString()
                          : "-"}
                      </td>
                      <td className="mono">{alert.source_ip || "-"}</td>
                      <td className="mono">
                        {alert.destination_ip || "-"}:
                        {alert.destination_port || "-"}
                      </td>
                      <td>{alert.alert_type || "-"}</td>
                      <td>
                        <SeverityBadge severity={alert.severity} />
                      </td>
                      <td>
                        <RiskBar score={alert.risk_score} />
                      </td>
                      <td>
                        <span className="status-badge">
                          {alert.status || "NEW"}
                        </span>
                      </td>
                      <td>
                        <button
                          className="view-button"
                          onClick={() => setSelectedAlert(alert)}
                        >
                          View
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </section>
      </main>

      {selectedAlert && (
        <div
          className="modal-backdrop"
          onClick={() => setSelectedAlert(null)}
        >
          <div
            className="modal"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="modal-header">
              <div>
                <h2>Alert Investigation</h2>
                <p>{selectedAlert.alert_id}</p>
              </div>

              <button
                className="close-button"
                onClick={() => setSelectedAlert(null)}
              >
                ×
              </button>
            </div>

            <div className="alert-detail-grid">
              <div>
                <label>Source IP</label>
                <strong>{selectedAlert.source_ip || "-"}</strong>
              </div>

              <div>
                <label>Destination IP</label>
                <strong>{selectedAlert.destination_ip || "-"}</strong>
              </div>

              <div>
                <label>Protocol</label>
                <strong>{selectedAlert.protocol || "-"}</strong>
              </div>

              <div>
                <label>Destination Port</label>
                <strong>{selectedAlert.destination_port || "-"}</strong>
              </div>

              <div>
                <label>Rule</label>
                <strong>{selectedAlert.rule_id || "-"}</strong>
              </div>

              <div>
                <label>Severity</label>
                <SeverityBadge severity={selectedAlert.severity} />
              </div>

              <div>
                <label>Risk Score</label>
                <strong>
                  {Number(selectedAlert.risk_score || 0).toFixed(1)}
                </strong>
              </div>

              <div>
                <label>Status</label>
                <strong>{selectedAlert.status || "NEW"}</strong>
              </div>
            </div>

            <div className="description-box">
              <label>Description</label>
              <p>
                {selectedAlert.description ||
                  "No additional description available."}
              </p>
            </div>

            <div className="investigation-box">
              <h3>Defensive Investigation</h3>
              <ul>
                <li>Review the source and destination addresses.</li>
                <li>Check the matched detection rule.</li>
                <li>Compare the event with the normal traffic baseline.</li>
                <li>Review related alerts from the same source.</li>
                <li>Record the analyst decision and resolution.</li>
              </ul>
            </div>

            <div className="modal-actions">
              <button
                onClick={() =>
                  updateAlertStatus(
                    selectedAlert.alert_id,
                    "INVESTIGATING"
                  )
                }
              >
                Investigating
              </button>

              <button
                onClick={() =>
                  updateAlertStatus(
                    selectedAlert.alert_id,
                    "RESOLVED"
                  )
                }
              >
                Resolve
              </button>

              <button
                onClick={() =>
                  updateAlertStatus(
                    selectedAlert.alert_id,
                    "FALSE_POSITIVE"
                  )
                }
              >
                False Positive
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);