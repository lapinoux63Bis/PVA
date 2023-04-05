from scapy.all import *
import socket
import os
import time
import csv

## Il semble impossible d'enregistrer des paquets localhost dans un fichier pcap ??

# Définition des paramètres de capture
interface = 'Wi-Fi' # interface réseau à écouter pour du localhost Software Loopback Interface 1
capture_duration = 8 # durée de capture en secondes
os.remove('captured_packets.pcap') #on s'assure de la création d'un fichier vierge en supprimant l'ancien
fichier = open("captured_packets.pcap", 'a') # et en ouvrant et fermant immédiatement le nouveau
fichier.close()
output_file = "captured_packets.pcap"


# Fonction pour capturer les paquets et les écrire dans un fichier
def capture_packets():
    start_time = time.perf_counter() # temps de début de capture
    captured_packets = [] # liste pour stocker les paquets capturés
    pktdump = PcapWriter(output_file, append=True)

    # Boucle de capture des paquets
    while True: #time.perf_counter() - start_time < capture_duration:
        packets = sniff(iface=interface, count=10) # capture de 10 paquets à la fois
        captured_packets += packets
        pktdump.write(packets)


    #print(f"Captured {len(captured_packets)} packets and saved to {output_file}")

# Appel de la fonction pour capturer les paquets
capture_packets()

## Obsolète
# packets=rdpcap('captured_packets.pcap')
#
# with open("registre_transmissions.csv", "a", newline ='') as csvfile:
#     write = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for packet in packets:
#         #print(packet.summary())
#         # Heure de transmission
#         timestamp = packet.time
#         print('Temps :', timestamp) #timestamp - base_time
#
#         # Ports source et destination
#         src_port = packet.sport
#         dst_port = packet.dport
#         print('Port Source :', src_port, '| Port Reception : ', dst_port)
#
#         # Protocole utilisé si en dehors de l'ordinateur
#         try:
#             port = socket.getservbyport(dst_port)
#             print('Protocole : ', port)
#         except OSError:
#             print('Erreur: Pas de protocole correspondant au port specifie')
#
#         # Adresses IP source et destination
#         src_ip = packet[IP].src
#         dst_ip = packet[IP].dst
#         print('IP source : ', src_ip, '| IP Reception : ', dst_ip)
#         print('\n')
#         write.writerow([timestamp, src_port, dst_port, port, src_ip, dst_ip])


#taille du paquet à récupérer


