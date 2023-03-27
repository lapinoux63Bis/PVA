import subprocess

# Lancer les scripts dans des processus distincts
p2 = subprocess.Popen(['python', 'sender.py'])
p1 = subprocess.Popen(['python', 'receiver.py'])
p3 = subprocess.Popen(['python', 'Capture_de_paquet.py'])

# Attendre que tous les processus se terminent
p3.wait()

subprocess.Popen.kill(p1)
subprocess.Popen.kill(p2)
