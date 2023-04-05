from scapy.all import *
import socket
import time
import csv

packets=rdpcap('captured_packets.pcap')

with open("registre_transmissions.csv", "w", newline ='') as csvfile:
    write = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for packet in packets:
        #print(packet.summary())
        # Heure de transmission
        timestamp = packet.time
        #print('Temps :', timestamp) #timestamp - base_time

        # Ports source et destination

        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        #src_port = packet.sport
        #dst_port = packet.dport

        #print('Port Source :', src_port, '| Port Reception : ', dst_port)

        # Protocole utilisé si en dehors de l'ordinateur
        try:
            proto = socket.getservbyport(dst_port)
            #print('Protocole : ', port)
        except (OSError, NameError):
            proto = ''
            #print('Erreur: Pas de protocole correspondant au port specifie')

        # Adresses IP source et destination
        if not IP in packet:
            src_ip = 'Unknown'
            dst_ip = 'Unknown'
        else:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst

        #print('IP source : ', src_ip, '| IP Reception : ', dst_ip)
        #print('\n')
        write.writerow([timestamp, src_port, dst_port, proto, src_ip, dst_ip])
