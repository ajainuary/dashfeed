import sqlite3
import string
from random import *
def register(email):
	connection = sqlite3.connect('user.db')
	cursor=connection.cursor() 
	characters = string.ascii_letters + string.punctuation  + string.digits
	password =  "".join(choice(characters) for x in range(randint(8, 16)))
	try:
		cursor.execute('''INSERT INTO user( email, password)VALUES(?,?)''', ( email,password))
		connection.commit()
	finally:
		connection.close()