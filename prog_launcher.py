import subprocess

# Lancer les scripts dans des processus distincts

#p2 = subprocess.Popen(['python', 'sender.py'])
#p1 = subprocess.Popen(['python', 'receiver.py'])

p3 = subprocess.Popen(['python', 'Capture_de_paquet.py'])
mail = subprocess.Popen(['python', 'mail_sender.py'])



# Attendre que tous les processus se terminent
p3.wait()
subprocess.Popen.kill(mail)

#p2.wait() #si p2 tourne avec while true, il n'y a pas d'écriture dans le fichier csv...
#subprocess.Popen.kill(p1)

