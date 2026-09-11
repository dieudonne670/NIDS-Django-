# 🛡️ Network Intrusion Detection System (NIDS)

A hybrid **Network Intrusion Detection System (NIDS)** built with Django, Scapy, PostgreSQL, and Machine Learning.

The system captures live network traffic, analyzes packets using rule-based detection techniques and an Isolation Forest anomaly-detection model, stores traffic data in PostgreSQL, and provides a web-based monitoring dashboard for security analysis.

🌐 **Live Dashboard:** https://nids-django.onrender.com/

📦 **GitHub Repository:** https://github.com/dieudonne670/NIDS-Django-

---

## 📌 Project Overview

Network Intrusion Detection Systems monitor network traffic to identify suspicious or potentially malicious activity.

This project implements a hybrid detection approach combining:

- 🔍 Rule-based intrusion detection
- 🤖 Machine Learning anomaly detection
- 📡 Real-time packet capture
- 🗄️ PostgreSQL data storage
- 📊 Web-based monitoring dashboard
- 📄 CSV and PDF security reports

The system is designed primarily as an educational and portfolio project demonstrating practical concepts in:

- Network security
- Python development
- Django
- Machine Learning
- Packet analysis
- PostgreSQL
- Linux networking
- Cloud deployment

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │      Network Traffic    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Scapy Sniffer      │
                    │   Live Packet Capture   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Detection Engine     │
                    │                         │
                    │  • Port Scan            │
                    │  • SYN Flood            │
                    │  • ICMP Flood           │
                    │  • SSH Brute Force      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   ML Anomaly Detection  │
                    │                         │
                    │    Isolation Forest     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    PostgreSQL / Neon    │
                    │       Database          │
                    └────────────┬────────────┘
                                 │
                                 ▼
              ┌────────────────────────────────────┐
              │        Django Web Dashboard        │
              │                                    │
              │  • Traffic Monitoring              │
              │  • Security Alerts                 │
              │  • Attack Statistics               │
              │  • Charts & Analytics              │
              │  • Reports                         │
              └────────────────────────────────────┘
                                 │
                                 ▼
                         🌐 Render Cloud



🚀 Key Features
📡 Real-Time Packet Capture

The system uses Scapy to capture live packets from a network interface on the monitoring machine.

Captured traffic can include information such as:

Source IP
Destination IP
Source port
Destination port
Protocol
Packet size
TCP flags
Timestamp

The captured information is stored in PostgreSQL for analysis and visualization.

🔍 Rule-Based Intrusion Detection

The detection engine currently identifies several common attack patterns.

1. Port Scan Detection

Detects suspicious activity involving attempts to access multiple ports on a host.

Purpose:

Identify reconnaissance activity where an attacker attempts to discover available services.

2. SYN Flood Detection

Detects unusually high volumes of TCP SYN packets.

Purpose:

Identify potential TCP SYN flood / denial-of-service activity.

3. ICMP Flood Detection

Detects unusually high volumes of ICMP traffic.

Purpose:

Identify potential ICMP-based denial-of-service activity.

4. SSH Brute Force Detection

Monitors repeated SSH connection attempts.

Purpose:

Identify suspicious authentication activity against SSH services.

🤖 Machine Learning Detection

The project also includes an unsupervised Machine Learning component using:

Isolation Forest

Isolation Forest is an anomaly-detection algorithm that attempts to identify observations that differ significantly from normal traffic patterns.

The ML component is useful because traditional rules are designed around known patterns, while anomaly detection can highlight unusual traffic that does not necessarily match one of the predefined rules.


Detection Approach

Normal Traffic
      │
      ▼
Feature Extraction
      │
      ▼
Isolation Forest
      │
      ├── Normal
      │
      └── Anomaly


The project therefore combines:
Known Attack Patterns
        +
Machine Learning Anomalies
        =
Hybrid NIDS


Note: Isolation Forest is an anomaly detector, not a supervised attack classifier. An anomaly should therefore be treated as suspicious rather than automatically considered a confirmed attack.

📊 Web Dashboard

The Django dashboard provides a centralized interface for monitoring captured traffic and detected security events.

The dashboard includes:

📈 Traffic statistics
🚨 Security alerts
🌐 Protocol distribution
📊 Attack/event statistics
🕒 Traffic timeline
📋 Traffic logs
📄 CSV export
📑 PDF reports
🔄 Automatic dashboard updates

Dashboard

Live:
https://nids-django.onrender.com/

🗄️ Database

The application uses PostgreSQL for persistent storage.

For the deployed version, PostgreSQL is hosted using Neon while the Django application is hosted on Render.

This allows the local packet-capture process and the cloud-hosted Django dashboard to work with the same database.


Local Computer
     │
     │ Scapy packet capture
     ▼
PostgreSQL / Neon
     ▲
     │
     │ Database queries
     │
Render
     │
     ▼
Django Dashboard

This architecture is particularly useful because cloud hosting platforms generally cannot directly access the physical network interface of a developer's local machine.

☁️ Deployment

The Django application is deployed on:

Render

The PostgreSQL database is hosted on:

Neon

Production Components

| Component                   | Technology                   |
| --------------------------- | ---------------------------- |
| Backend                     | Django                       |
| Web Server                  | Gunicorn                     |
| Packet Capture              | Scapy                        |
| Database                    | PostgreSQL                   |
| Cloud Database              | Neon                         |
| Machine Learning            | Scikit-learn                 |
| ML Algorithm                | Isolation Forest             |
| Frontend                    | Django Templates / Bootstrap |
| Charts                      | Chart.js                     |
| PDF Reports                 | ReportLab                    |
| Hosting                     | Render                       |
| Operating System for Sensor | Linux                        |

🧰 Technology Stack

| Category                | Technology           |
| ----------------------- | -------------------- |
| Programming Language    | Python               |
| Web Framework           | Django               |
| Packet Analysis         | Scapy                |
| Machine Learning        | Scikit-learn         |
| ML Algorithm            | Isolation Forest     |
| Database                | PostgreSQL           |
| Database Hosting        | Neon                 |
| Web Hosting             | Render               |
| Web Server              | Gunicorn             |
| Frontend                | HTML, CSS, Bootstrap |
| Visualization           | Chart.js             |
| Reporting               | ReportLab            |
| Version Control         | Git / GitHub         |
| Development Environment | Linux / Ubuntu       |


📁 Project Structure

NIDS/
│
├── dashboard/
│   ├── templates/
│   │   └── dashboard/
│   │       ├── alerts.html
│   │       ├── index.html
│   │       ├── reports.html
│   │       └── traffic.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── detection_engine/
│   ├── migrations/
│   ├── detection.py
│   └── ...
│
├── ml_module/
│   ├── migrations/
│   ├── models.py
│   └── ...
│
├── packet_capture/
│   ├── migrations/
│   ├── sniffer.py
│   └── ...
│
├── nids_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

💻 Local Installation
1. Clone the repository
git clone https://github.com/dieudonne670/NIDS-Django-.git
cd NIDS-Django-
2. Create a virtual environment
python3 -m venv venv

Activate it:

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file in the project root:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-postgresql-connection-string

Do not commit .env to GitHub.

5. Apply migrations
python manage.py migrate
6. Start the Django development server
python manage.py runserver

Open:

http://127.0.0.1:8000/
📡 Running the Network Sensor

The packet sniffer must run on a machine that has access to the network interface being monitored.

For Linux:

sudo python packet_capture/sniffer.py

Depending on the project's current implementation, the correct Python environment may need to be used:

sudo ./venv/bin/python packet_capture/sniffer.py

The sniffer captures traffic and stores the resulting information in the configured PostgreSQL database.

🧪 Testing the Detection Engine

The system can be tested in a controlled environment using traffic patterns corresponding to the supported detection rules.

Examples include:

Port scanning
TCP SYN traffic spikes
ICMP traffic spikes
Repeated SSH connection attempts

Only perform security testing against systems and networks that you own or have explicit permission to test.

🔐 Security Considerations

The project follows several basic security practices:

Environment variables are used for secrets and database credentials.
.env should not be committed to Git.
Production DEBUG should remain disabled.
PostgreSQL is used instead of storing production data in local files.
The cloud database connection uses an encrypted connection.
The packet-capture component runs separately from the public web dashboard.

For a production-grade deployment, additional controls would be required, including:

Authentication and authorization
HTTPS enforcement
Rate limiting
Network segmentation
Centralized logging
SIEM integration
Secure alert delivery
Database hardening
Secret rotation
Monitoring and observability
⚠️ Current Architecture Limitation

The live packet-capture component runs on the local monitoring machine because the Render web service does not have direct access to that machine's physical network interface.

Therefore, the current architecture is:

Local Linux Machine
       │
       │ Scapy
       ▼
Packet Capture
       │
       ▼
Neon PostgreSQL
       ▲
       │
       │
Render Django
       │
       ▼
Web Dashboard


🔮 Future Improvements

Potential future versions could introduce:

Detection
ARP spoofing detection
UDP flood detection
DNS attack detection
HTTP flood detection
DNS tunneling detection
More advanced traffic features
Behavioral profiling
Machine Learning
Supervised attack classification
Random Forest
XGBoost
Autoencoders
Neural-network-based anomaly detection
Evaluation using labeled datasets
Precision / Recall / F1-score benchmarking
Distributed Architecture

A future architecture could look like:

             ┌───────────────┐
             │ Network Sensor│
             │       #1      │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │               │
             │ Message/API   │
             │    Layer      │
             │               │
             └───────┬───────┘
                     │
          ┌──────────▼──────────┐
          │ Central Detection    │
          │ Engine + ML          │
          └──────────┬──────────┘
                     │
             ┌───────▼───────┐
             │   PostgreSQL  │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Django         │
             │ Dashboard      │
             └───────────────┘

Possible technologies for a future distributed version include:

Kafka
Redis
Celery
FastAPI
Docker
Kubernetes
Elasticsearch
Grafana
SIEM integration


📚 Learning Objectives

This project was developed to demonstrate practical understanding of:

Network packet analysis
Intrusion detection
TCP/IP networking
Python programming
Django web development
PostgreSQL database management
Machine Learning
Linux networking
Cloud deployment
Git/GitHub workflows
Security monitoring


⚠️ Disclaimer

This project is intended for:

Educational purposes
Academic research
Authorized security testing
Portfolio demonstration

It should not be considered a complete enterprise-grade security solution.

Do not use the system to monitor or attack networks without proper authorization.

👨‍💻 Author

Kindong Dieudonne: Software Engineer / Backend Developer 

GitHub:
https://github.com/dieudonne670


