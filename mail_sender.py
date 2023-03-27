#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import sys
import smtplib

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
					<p style ="margin: 5px 0;line-height: 25px;">coucou {},<br>
					<br>
					Allons manger Miam j'ai faim.
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
		self.fromaddr = "gabriel.flotte@hotmail.fr"# alias
		self.password = "kofrlfeisitwaqwy"#


	def sendMessageViaServer(self,toaddr,msg):
		# Send the message via local SMTP server.
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self.logaddr, self.password)
		text = msg.as_string()
		server.sendmail(self.fromaddr, toaddr, text)
		server.quit()



	def sendHtmlEmailTo(self,destName,destinationAddress,msgBody):
		#Message setup
		msg = MIMEMultipart()

		msg['From'] =  "Me<"+self.fromaddr+">"
		msg['To'] = destinationAddress
		msg['Subject'] = "Hello mail"

		hostname=sys.platform


		txt = EMAIL_HTML_TEMPLATE

		txt=txt.format(destName,msgBody,hostname)

		#Add text to message
		msg.attach(MIMEText(txt, 'html'))

		print("Send email from {} to {}".format(self.fromaddr,destinationAddress))
		self.sendMessageViaServer(destinationAddress,msg)



if __name__ == "__main__":
	email= EmailSenderClass()
	email.sendHtmlEmailTo("Admin","gabriel.flotte@hotmail.fr","Ceci est un mail automatique envoyé à partir d'un script Python. BISOUS <3")