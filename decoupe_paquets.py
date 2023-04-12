import csv
import os
import glob
from scapy.all import *

file = "captured_packets.pcap"
actions = []

with open("registre_actions.csv", newline = '') as csvfile:
    read = csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in read:
        actions.append(row)

if actions[0] == []:
    actions.remove([])
print(actions)

for rfile in glob('./mini_*'):
    os.remove(rfile)

for i in range (len(actions)):
    time1 = float(actions[i][0])
    time2 = float(actions[i][1])
    j = str(i)
    output_file = "mini_packets_"+j+"_.pcap"
    packets = rdpcap(file)
    pktdump = PcapWriter(output_file, append=True)
    paquito = []

    for packet in packets:
        if (packet.time <= time2) and (packet.time >= time1):
            paquito += packet

    pktdump.write(paquito)

    print(time1, time2)