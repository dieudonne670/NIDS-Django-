from collections import defaultdict
from datetime import datetime

syn_tracker = defaultdict(list)

def detect_syn_flood(packet):

    from scapy.all import IP, TCP

    if IP not in packet or TCP not in packet:
        return None

    # SYN flag only
    if packet[TCP].flags != "S":
        return None

    source_ip = packet[IP].src

    syn_tracker[source_ip].append(datetime.now())

    syn_count = len(syn_tracker[source_ip])

    print(
        f"SYN DEBUG: {source_ip} -> {syn_count} SYN packets"
    )

    if syn_count >= 50:

        return {
            "source_ip": source_ip,
            "attack_type": "SYN_FLOOD",
            "severity": "CRITICAL",
            "description": f"Possible SYN Flood attack from {source_ip}"
        }

    return None