import sys
# import os
# import signal
import subprocess
# from typing import get_type_hints
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QProcess, Qt


pid: int

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

        self.end_button.setEnabled(False)

        self.start_button.clicked.connect(self.start_record)
        self.end_button.clicked.connect(self.end_record)
        self.mail_button.clicked.connect(self.send_mail)
        self.selenium_button.clicked.connect(self.start_selenium)

        layout.addWidget(self.start_button, 0, 0)
        layout.addWidget(self.mail_button, 0, 1)
        layout.addWidget(self.end_button, 1, 0)
        layout.addWidget(self.selenium_button, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.process = QProcess()

    def start_record(self, cap):
        self.process.start('python', ['Capture_de_paquet.py'])
        self.start_button.setEnabled(False)
        self.end_button.setEnabled(True)
        print("Record started")

        #cap = subprocess.Popen(['python', 'Capture_de_paquet.py'])
        #pid = cap.pid

    def end_record(self, cap):
        #self.process.waitForFinished()

        self.process.kill()
        ecriture = subprocess.Popen(['python', 'ecriture.py'])
        ecriture.wait()
        self.start_button.setEnabled(True)
        self.end_button.setEnabled(False)
        print("Record ended")

        #os.kill(cap.pid, signal.SIGTERM)
        #cap.terminate()
        #subprocess.Popen.kill(cap) #à voir
        #os.kill(pid, signal.TERM)

    def send_mail(self):
        mail = subprocess.Popen(['python', 'mail_sender.py'])
        mail.wait()
        print("Mail sent")

    def start_selenium(self):
        selenium = subprocess.Popen(['python', 'selenium_.py'])
        selenium.wait()
        print("Selenium launched")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()