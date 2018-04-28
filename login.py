import sqlite3

def login(email,password):
	conn = sqlite3.connect('user.db')
	cursor = conn.cursor()
	sql = """select from user where email="{p}" and password="{q}" ; """
	sql = sql.format(p=email,q=)
	ro = cursor.execute(sql)
	customers = ro.fetchall()
	return customers