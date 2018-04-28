import sqlite3
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import *
def register(email):
	connection = sqlite3.connect('user.db')
	cursor=connection.cursor() 
	characters = string.ascii_letters + string.punctuation  + string.digits
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("dashfeed07@gmail.com", "Dashfeed2018")
	password =  "".join(choice(characters) for x in range(randint(8, 16)))
	msg = "Welcome to DashFeed,\nWe're excited to have you onboard our news platform.\nHere's your password (Let's keep it a secret!): "+password
	message = 'Subject: {}\n\n{}'.format("Welcome to DashFeed",msg)
	server.sendmail("dashfeed07@gmail.com",email,message)
	server.quit()
	try:
		cursor.execute('''INSERT INTO user( email, password)VALUES(?,?)''', ( email,password))
		connection.commit()
	finally:
		connection.close()


