from collections import defaultdict
from datetime import datetime

icmp_tracker = defaultdict(list)

def detect_icmp_flood(packet):

    from scapy.all import IP, ICMP

    if IP not in packet or ICMP not in packet:
        return None

    source_ip = packet[IP].src

    icmp_tracker[source_ip].append(datetime.now())

    icmp_count = len(icmp_tracker[source_ip])

    print(
        f"ICMP DEBUG: {source_ip} -> {icmp_count}"
    )

    if icmp_count >= 20:

        return {
            "source_ip": source_ip,
            "attack_type": "ICMP_FLOOD",
            "severity": "HIGH",
            "description": f"ICMP Flood detected from {source_ip}"
        }

    return None