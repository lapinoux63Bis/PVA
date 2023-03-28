import socket

UDP_IP_SRC = "172.17.0.2"
UDP_IP_DST = "172.17.0.1"
UDP_PORT_SENDER = 12346
UDP_PORT_RECEIVER = 12345

listener_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listener_sock.bind((UDP_IP_SRC, UDP_PORT_RECEIVER))

while True:
    data = listener_sock.recvfrom(1024)

    if data[0].decode() == "send_mail":
        sender_sock.sendto(b"Mail sent...", (UDP_IP_DST, UDP_PORT_SENDER))
    else:
        sender_sock.sendto(b"Bad command", (UDP_IP_DST, UDP_PORT_SENDER))
