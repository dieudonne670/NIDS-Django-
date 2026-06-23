import os
import sys

# ==========================
# Django Setup
# ==========================
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, BASE_DIR)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "nids_project.settings"
)

import django
django.setup()

# ==========================
# Imports
# ==========================
from scapy.all import packet, sniff, IP, TCP, UDP, ICMP
from detection_engine.syn_flood import detect_syn_flood
from detection_engine.icmp_flood import detect_icmp_flood
from detection_engine.brute_force import detect_brute_force

from packet_capture.models import TrafficLog
from detection_engine.models import Alert
from detection_engine.port_scan import detect_port_scan


# ==========================
# Packet Processing
# ==========================
def process_packet(packet):

    if IP not in packet:
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    protocol = "OTHER"
    source_port = None
    destination_port = None

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"

    # Save traffic log
    TrafficLog.objects.create(
        source_ip=source_ip,
        destination_ip=destination_ip,
        protocol=protocol,
        source_port=source_port,
        destination_port=destination_port,
        packet_size=len(packet)
    )

    print(
        f"{source_ip} -> {destination_ip} "
        f"{protocol}"
    )

    # Port Scan
    alert = detect_port_scan(packet)
    if alert:
        Alert.objects.create(**alert)
        print(f"[ALERT] {alert['attack_type']}")

    # SYN Flood
    syn_alert = detect_syn_flood(packet)

    if syn_alert:
        Alert.objects.create(**syn_alert)
        print(f"[ALERT] {syn_alert['attack_type']}")

    # ICMP Flood
    icmp_alert = detect_icmp_flood(packet)

    if icmp_alert:
        Alert.objects.create(**icmp_alert)
        print(f"[ALERT] {icmp_alert['attack_type']}")

    # Brute Force
    brute_alert = detect_brute_force(packet)

    if brute_alert:
        Alert.objects.create(**brute_alert)
        print(f"[ALERT] {brute_alert['attack_type']}")

    # ==========================
    # Port Scan Detection
    # ==========================
    alert = detect_port_scan(packet)

    if alert:

        Alert.objects.create(
            source_ip=alert["source_ip"],
            attack_type=alert["attack_type"],
            severity=alert["severity"],
            description=alert["description"]
        )

        print(
            f"[ALERT] {alert['attack_type']} "
            f"from {alert['source_ip']}"
        )


 #============================
 #port scan detection for syn_flood
 #============================
    syn_alert = detect_syn_flood(packet)

    if syn_alert:

        Alert.objects.create(
            source_ip=syn_alert["source_ip"],
            attack_type=syn_alert["attack_type"],
            severity=syn_alert["severity"],
            description=syn_alert["description"]
        )

        print(
            f"[CRITICAL] {syn_alert['attack_type']} "
            f"from {syn_alert['source_ip']}"
        )

# ==========================
# Start Sniffer
# ==========================
print("NIDS Sniffer Started...")

sniff(
    prn=process_packet,
    store=False
)
