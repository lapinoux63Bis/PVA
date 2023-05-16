import pyshark
import csv


interface = 'en0'  # Interface réseau
capture_duration = 10  # Durée de capture en secondes
output_file = 'packet_capture.csv'  # Nom du fichier de sortie


def capture_packets(interface, duration, output_file):
    capture = pyshark.LiveCapture(interface)
    capture.sniff(timeout=duration)

    with open(output_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Temps", "Port Source", "Port de destination", "Protocole", 'IP Source', 'IP d destination' ])

        for packet in capture:
            time = packet.sniff_time
            src_port = packet.tcp.srcport if 'tcp' in packet else ''
            dst_port = packet.tcp.dstport if 'tcp' in packet else ''
            protocol = packet.transport_layer
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            writer.writerow([time, src_port, dst_port, protocol, src_ip, dst_ip])

#if __name__ == '__main__':
#interface = 'en0'  
#capture_duration = 10 
#output_file = 'packet_capture.csv' 

capture_packets(interface, capture_duration, output_file)
