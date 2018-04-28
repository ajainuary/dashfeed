import sqlite3
conn = sqlite3.connect('user.db')
c=conn.cursor()
c.execute("CREATE TABLE user(id integer PRIMARY KEY AUTOINCREMENT,\
	email text,password text,preference1 text,preference2 text,read longtext)")
conn.commit()
conn.close()