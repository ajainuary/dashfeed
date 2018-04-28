import sqlite3

def login(email,password):
	conn = sqlite3.connect('user.db')
	cursor = conn.cursor()
	sql = """select from user where email like "%{p}%"; """
	sql = sql.format(p=category)
	ro = cursor.execute(sql)
	customers = ro.fetchall()
	return customers