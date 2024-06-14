from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f"IP Packet: {ip_src} -> {ip_dst} (Protocol: {protocol})")

        # Check if the packet has a TCP layer
        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"TCP Segment: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

        # Check if the packet has a UDP layer
        elif UDP in packet:
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f"UDP Segment: {ip_src}:{udp_sport} -> {ip_dst}:{udp_dport}")


sniff(iface="Wi-Fi 3", filter="ip", prn=packet_callback, store=0)