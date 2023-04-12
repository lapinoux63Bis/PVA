import sys
import time
# import os
# import signal
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QProcess, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ActivityRecorder")
        self.setWindowIcon(QIcon("record.svg"))
        self.setFixedSize(300, 150)

        layout = QGridLayout()

        self.start_button = QPushButton("Start record")
        self.end_button = QPushButton("End record")
        self.mail_button = QPushButton("Send mail")
        self.selenium_button = QPushButton("Launch Selenium")
        self.mini_paquet = QPushButton("Découpage des paquets")

        self.end_button.setEnabled(False)

        self.start_button.clicked.connect(self.start_record)
        self.end_button.clicked.connect(self.end_record)
        self.mail_button.clicked.connect(self.send_mail)
        self.selenium_button.clicked.connect(self.start_selenium)
        self.mini_paquet.clicked.connect(self.decoupe_paquet)

        layout.addWidget(self.start_button, 0, 0)
        layout.addWidget(self.mail_button, 0, 1)
        layout.addWidget(self.end_button, 1, 0)
        layout.addWidget(self.selenium_button, 1, 1)
        layout.addWidget(self.mini_paquet)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.process = QProcess()

    def start_record(self, cap):
        timestamp = time
        self.process.start('python', ['Capture_de_paquet.py'])
        self.start_button.setEnabled(False)
        self.end_button.setEnabled(True)
        print("Record started")

    def end_record(self, cap):
        self.process.kill()
        ecriture = subprocess.Popen(['python', 'ecriture.py'])
        ecriture.wait()
        self.start_button.setEnabled(True)
        self.end_button.setEnabled(False)
        print("Record ended")

    def send_mail(self):
        mail = subprocess.Popen(['python', 'mail_sender.py'])
        mail.wait()
        print("Mail sent")

    def start_selenium(self):
        selenium = subprocess.Popen(['python', 'selenium_.py'])
        selenium.wait()
        print("Selenium launched")

    def decoupe_paquet(self):
        print("découpage des paquets en fonction des actions enregistrées")
        decoup = subprocess.Popen(['python', 'decoupe_paquets.py'])
        decoup.wait()
        print('Paquets récupérés')
        #certains paquets d'une même transmission sont manquants
        #certains paquets passent



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()