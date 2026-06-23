from collections import defaultdict
from datetime import datetime

ssh_tracker = defaultdict(list)

def detect_brute_force(packet):

    from scapy.all import IP, TCP

    if IP not in packet or TCP not in packet:
        return None

    if packet[TCP].dport != 22:
        return None

    source_ip = packet[IP].src

    ssh_tracker[source_ip].append(datetime.now())

    attempts = len(ssh_tracker[source_ip])

    print(
        f"SSH DEBUG: {source_ip} -> {attempts}"
    )

    if attempts >= 10:

        return {
            "source_ip": source_ip,
            "attack_type": "BRUTE_FORCE",
            "severity": "HIGH",
            "description": f"Possible SSH brute force attack from {source_ip}"
        }

    return None