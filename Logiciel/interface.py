import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ActivityRecorder")
        self.setWindowIcon(QIcon("record.svg"))
        self.setFixedSize(300, 150)

        layout = QGridLayout()

        start_button = QPushButton("Start record")
        mail_button = QPushButton("Send mail")
        start_button.clicked.connect(self.start_record)
        mail_button.clicked.connect(self.send_mail)

        layout.addWidget(start_button, 0, 0)
        layout.addWidget(mail_button, 0, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def start_record(self):
        print("Start record...")

    def send_mail(self):
        print("Mail sent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
