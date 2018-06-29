'''
This file contains the postman class that handles the sending of mails via
the gmail smtp server, it takes a single input mail during input and then can
send it to the email id sent to the sendmessage method.
'''


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import getpass

import os
  
class PostMan:

	def __init__(self,fromU, sub, body, attach = None):
		self.fromU = fromU
		self.sub = sub
		self.body = body
		self.attach = attach
		self.password = getpass.getpass(prompt = "password for " + str(self.fromU)+": ")
		self.server = smtplib.SMTP('smtp.gmail.com', 587)

	def login(self):
		self.server.starttls()
		self.server.login(self.fromU,self.password)

	def sendMessage(self,toU, toN):
		msg = MIMEMultipart()
		msg['From'] = self.fromU
		msg['To'] = toU
		msg['Subject'] = self.sub
		body = self.body.format(toN)
		if self.attach:
			msg.attach(MIMEText(body, 'plain'))
			filename = self.attach
			attachment = open(os.path.dirname(os.path.realpath(__file__))+'/'+self.attach, "rb")
			p = MIMEBase('application', 'octet-stream')
			p.set_payload((attachment).read())
			encoders.encode_base64(p)
			p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
			msg.attach(p)
		text = msg.as_string()
		return self.server.sendmail(self.fromU, toU, text)

	def quit(self):
		self.password = None
		self.server.quit()