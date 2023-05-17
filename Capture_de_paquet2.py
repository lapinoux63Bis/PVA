import pyshark
import csv
import nest_asyncio
import socket

nest_asyncio.apply() #Règle le problème de double boucle avec Spyder

interface = 'en0'  # Interface réseau (en0 —> WiFi; en0 —> localhost)
capture_duration = 5  # Durée de capture en secondes
output_file = 'packet_capture.csv'  # Nom du fichier de sortie


def capture_packets(interface, duration, output_file):
    capture = pyshark.LiveCapture(interface)
    capture.sniff(timeout=duration)

    with open(output_file, 'a', newline='') as file :
        writer = csv.writer(file, delimiter = ';', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Temps", "Port Source", "Port de destination", "Protocole", 'IP Source', 'IP de destination' ])
        for packet in capture:
            time = packet.sniff_time
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            protocol = packet.highest_layer
            if 'tcp' in packet : 
                src_port = packet.tcp.srcport 
                dst_port = packet.tcp.dstport
            if 'udp' in packet :
                src_port = packet.udp.srcport
                dst_port = packet.udp.dstport
            else :
                src_port = "Pas de port source"
                dst_port = "Pas de port de destination"

            writer.writerow([time, src_port, dst_port, protocol, src_ip, dst_ip])



capture_packets(interface, capture_duration, output_file)
