# 🛡️ NIDS v2 – Network Intrusion Detection System

> A Machine Learning-powered Network Intrusion Detection System built with Django, Scapy, PostgreSQL and Scikit-learn.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Machine Learning](https://img.shields.io/badge/ML-IsolationForest-orange)
![License](https://img.shields.io/badge/License-MIT-red)

---

# 📌 Overview

NIDS v2 is a real-time Network Intrusion Detection System designed to monitor network traffic, detect suspicious activities, and visualize security events through a professional web dashboard.

Unlike signature-based IDS solutions, this project combines:

- Real-time packet capture
- Rule-based attack detection
- Machine Learning anomaly detection
- Interactive security dashboard
- PostgreSQL data storage

The project was developed for networking and cybersecurity education while following software engineering best practices.

---

# 🚀 Features

## Packet Capture

- Real-time packet sniffing using Scapy
- TCP detection
- UDP detection
- ICMP detection
- Packet size monitoring
- Source & destination IP logging
- Source & destination port logging

---

## Intrusion Detection Engine

### ✅ Port Scan Detection

Detects hosts scanning multiple ports within a short period.

---

### ✅ SYN Flood Detection

Detects excessive TCP SYN packets that indicate denial-of-service attacks.

---

### ✅ ICMP Flood Detection

Detects ICMP flooding attacks.

---

### ✅ Brute Force Detection

Monitors repeated authentication attempts on services such as SSH.

---

## Machine Learning

Isolation Forest based anomaly detection using multiple network features:

- Packet Size
- Protocol
- Source Port
- Destination Port

Automatically identifies abnormal traffic that rule-based detection may miss.

---

## Dashboard

Professional Django dashboard featuring:

- Live traffic statistics
- Attack counters
- Recent alerts
- Recent anomalies
- Protocol distribution
- Traffic analytics
- Auto refresh
- CSV report export
- PDF report export

---

# 🏗️ Project Architecture

```
               +---------------------+
               | Network Traffic     |
               +----------+----------+
                          |
                          |
                     Scapy Sniffer
                          |
                          |
             +------------+------------+
             |                         |
             |                         |
      Packet Logger             Detection Engine
             |                         |
             |         +---------------+--------------+
             |         |               |              |
             |    Port Scan      SYN Flood     ICMP Flood
             |                                   |
             |                              Brute Force
             |                                   |
             +----------------+------------------+
                              |
                              |
                        PostgreSQL Database
                              |
                 +------------+------------+
                 |                         |
          Django Dashboard         Machine Learning
                                        |
                                 Isolation Forest
                                        |
                                  Anomaly Detection
```

---

# 🛠 Technology Stack

Backend

- Python
- Django
- PostgreSQL

Packet Analysis

- Scapy

Machine Learning

- Scikit-learn
- Pandas
- NumPy

Reporting

- ReportLab

Frontend

- Bootstrap 5
- Chart.js
- HTML5
- CSS3

---

# 📂 Project Structure

```
NIDS/

├── dashboard/
├── detection_engine/
├── packet_capture/
├── ml_module/
├── nids_project/
├── requirements.txt
├── manage.py
└── README.md
```

---

# 📸 Dashboard

Features include:

- Security Overview
- Attack Statistics
- Live Traffic
- Alerts
- Anomalies
- Charts
- Reports

(Add screenshots here after deployment.)

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/NIDS.git

cd NIDS
```

---

## Create Virtual Environment

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key

DB_NAME=nids_db

DB_USER=postgres

DB_PASSWORD=your_password

DB_HOST=localhost

DB_PORT=5432

DEBUG=True
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Create Admin User

```bash
python manage.py createsuperuser
```

---

## Run Django

```bash
python manage.py runserver 8080
```

---

## Run Packet Sniffer

Linux

```bash
sudo -E ./venv/bin/python packet_capture/sniffer.py
```

---

## Run Machine Learning

```bash
python manage.py detect_anomalies
```

---

# Future Improvements

- Deep Learning Detection
- LSTM-based anomaly detection
- Auto-retraining
- Threat Intelligence feeds
- SIEM integration
- Elasticsearch
- Kibana dashboards
- Docker deployment
- Kubernetes support
- Email notifications
- Slack integration
- REST API
- WebSocket live monitoring

---

# Current Version

**NIDS v2**

Included:

- Rule-based Detection
- Machine Learning Detection
- Dashboard
- Reports
- Charts
- CSV Export
- PDF Export

---

# Planned Versions

## NIDS v3

- Deep Learning
- LSTM
- Auto Training
- Explainable AI
- Threat Intelligence

---

## NIDS v4

- Distributed Detection
- Microservices
- Kafka
- FastAPI
- Docker
- Kubernetes
- Real-time Streaming
- Cloud Deployment

---

# Author

**Kindong Dieudonne**

Backend Developer • Cybersecurity Enthusiast • Machine Learning Enthusiast

GitHub:
https://github.com/dieudonne670



# License

MIT License

Feel free to use this project for learning and educational purposes.
