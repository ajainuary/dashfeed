import sqlite3
def push_to_database(headline,subtitle,content,rating,link):
	connection = sqlite3.connect('../news.db')
	cursor=connection.cursor() 
	try:
		cursor.execute('''INSERT INTO NEWS( title, subject, content,rating,link)VALUES(?,?,?,?,?)''', ( headline, subtitle, content,rating,link))
		connection.commit()
	finally:
		connection.close()