import sqlite3
connection = sqlite3.connect('../news.db')
cursor=connection.cursor() 
try:
	cursor.execute("delete from NEWS where id>=139 and id<=153")
	connection.commit()
finally:
	connection.close()