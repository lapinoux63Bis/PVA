import socket
import time

UDP_IP_SRC = "172.17.0.1"
UDP_IP_DST = "172.17.0.2"
UDP_PORT_SENDER = 12345
UDP_PORT_RECEIVER = 12346

sender_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_sock.bind((UDP_IP_SRC, UDP_PORT_RECEIVER))

while True:
    print("Command : ")
    data = input().encode()
    sender_sock.sendto(data, (UDP_IP_DST, UDP_PORT_SENDER))
    data = receiver_sock.recvfrom(1024)
    print(data)
