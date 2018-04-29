import sqlite3
def validate(username, password):
    con = sqlite3.connect('../news.db')
    completion = None
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM user")
        rows = cur.fetchall()
        for row in rows:
            if row != None:
             dbUser = row[1]
             dbPass = row[2]
             if dbUser==username:
                 completion=check_password(dbPass, password)
                 if completion:
                 	return row[0]
    return completion
def check_password(dbPass,password):
    return dbPass == password