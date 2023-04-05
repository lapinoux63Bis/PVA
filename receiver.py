import socket
import time

IP = "localhost"
PORT = 1235

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sk.bind((IP, PORT))

start_time = time.time()
duration = 7

while True: #time.time() - start_time < duration
    data = sk.recvfrom(1024)
    print(data[0].decode())