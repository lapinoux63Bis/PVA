#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import sys
import smtplib
import time
import csv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import formataddr

EMAIL_HTML_TEMPLATE="""<html>
				  <head>
				  </head>
				  <body>
					<p style ="margin: 5px 0;line-height: 25px;">bonjour {},<br>
					<br>
					test de message automatique
					<br>
					{}
					<br>
					Bien à vous,<br>
					{} <br>
					</p>
				  </body>
				</html>
				"""


class EmailSenderClass:

	def __init__(self):
		""" """
		self.logaddr = "bagmanf1@gmail.com"
		self.fromaddr = "bagmanf1@gmail.com"# alias
		self.password = "kofrlfeisitwaqwy"#


	def sendMessageViaServer(self,toaddr,msg):
		# Send the message via local SMTP server.
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		timestamp1 =time.time()
		server.login(self.logaddr, self.password)
		text = msg.as_string()
		server.sendmail(self.fromaddr, toaddr, text)
		server.quit()
		return timestamp1



	def sendHtmlEmailTo(self,destName,destinationAddress,msgBody):
		#Message setup
		msg = MIMEMultipart()

		msg['From'] =  "Me<"+self.fromaddr+">"
		msg['To'] = destinationAddress
		msg['Subject'] = "TEST auto"

		hostname=sys.platform


		txt = EMAIL_HTML_TEMPLATE

		txt=txt.format(destName,msgBody,hostname)

		#Add text to message
		msg.attach(MIMEText(txt, 'html'))

		print("Send email from {} to {}".format(self.fromaddr,destinationAddress))
		timestamp1 = self.sendMessageViaServer(destinationAddress,msg)
		timestamp = time.time()
		return timestamp, timestamp1


with open("registre_actions.csv", "w", newline='') as csvfile:
	write = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	if __name__ == "__main__":
		email= EmailSenderClass()
		timestamp, timestamp1 = email.sendHtmlEmailTo("MOI","bagmanf1@gmail.com","mail automatique.'")
		write.writerow([timestamp1, timestamp, "", "", "", "smtp", ""])
