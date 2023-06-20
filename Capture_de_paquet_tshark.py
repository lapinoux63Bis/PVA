import subprocess
import csv

interface = 'en0'  # Remplacez 'eth0' par votre interface réseau
capture_duration = 10  # Durée de capture en secondes
output_file = 'packet_info.csv'  # Nom du fichier de sortie

def capture_packets(interface, duration):
    command = ['/usr/local/bin/tshark', '-i', interface, '-a', f'duration:{duration}', '-T', 'fields', '-e', 'frame.time', '-e', 'ip.src', '-e', 'ip.dst', '-e', 'tcp.srcport', '-e', 'tcp.dstport', '-e', 'udp.srcport', '-e', 'udp.dstport', '-e', 'frame.protocols']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    data = []

    for line in iter(process.stdout.readline, b''):
        packet_data = line.decode().strip().split('\t')
        if len(packet_data) >= 7:
            time = packet_data[0]
            src_ip = packet_data[1]
            dst_ip = packet_data[2]
            src_port = packet_data[3]
            dst_port = packet_data[4]
            udp_src_port = packet_data[5]
            udp_dst_port = packet_data[6]
            protocol = packet_data[7]

            data.append([time, src_ip, dst_ip, src_port, dst_port, udp_src_port, udp_dst_port, protocol])

    return data

def write_to_csv(data, output_file):
    
    with open("registre_transmissions.csv", "a") as csvfile:
        write = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(["Temps", 'IP Source', 'IP d destination', "Port Source TCP ", "Port de destination TCP ", "Port Source UDP ", "Port de destination UDP ", "Protocole" ])
        write.writerows(data)



captured_data = capture_packets(interface, capture_duration)
write_to_csv(captured_data, output_file)
