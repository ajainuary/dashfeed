import sqlite3
def validate(username, password):
    con = sqlite3.connect('../user.db')
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM users")
                rows = cur.fetchall()
                if rows != NULL
                    dbUser = row[1]
                    dbPass = row[2]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion