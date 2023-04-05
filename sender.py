import socket
import time
import csv

dst_ip = "localhost"
dst_port = 1235

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start_time = time.perf_counter()
duration = 6
with open("registre_actions.csv", "a", newline='') as csvfile:
    write = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    while time.perf_counter() - start_time < duration:
        sk.sendto(b"coucou", (dst_ip, dst_port))
        timestamp = time.time()
        write.writerow([timestamp, "", dst_port, "", "", dst_ip])
        time.sleep(2)
