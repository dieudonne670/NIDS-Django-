from collections import defaultdict

port_tracker = defaultdict(set)


def detect_port_scan(packet):

    from scapy.all import IP, TCP

    if IP not in packet or TCP not in packet:
        return None

    source_ip = packet[IP].src
    destination_port = packet[TCP].dport

    port_tracker[source_ip].add(destination_port)

    print(
        f"DEBUG: {source_ip} -> "
        f"{len(port_tracker[source_ip])} unique ports"
    )

    # Lower threshold for testing
    if len(port_tracker[source_ip]) >= 10:
        print("ALERT CONDITIO MET")

        return {
            "source_ip": source_ip,
            "attack_type": "PORT_SCAN",
            "severity": "HIGH",
            "description": f"Possible port scan detected from {source_ip}"
        }

    return None