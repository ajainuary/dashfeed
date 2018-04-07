import sqlite3
conn = sqlite3.connect('news.db')
c=conn.cursor()
 
 
# cursor.execute(sql)
task_1=(7, 'James', 'sda', 'Houston', 10000,'sad','sdasda' )
# create_task(conn,task_1)
c.execute("CREATE TABLE NEWS(ID longint,Title text,Subject text,Content longtext,Rating longint,Link text,Tags text)")
c.execute("INSERT INTO NEWS (ID,Title,Subject,Content,Rating,Link,Tags)VALUES (1, 'Paul', 'sda', 'California', 20000,'sda','sda' ); ")
c.execute("INSERT INTO NEWS VALUES (7, 'James', 'sda', 'Houston', 10000,'sad','sdasda' )");
c.execute("INSERT INTO NEWS VALUES (7, 'James', 'sda', 'Houston', 10000,'sad','sdasda' )");
c.execute("INSERT INTO NEWS VALUES (7, 'James', 'sda', 'Houston', 10000,'sad','sdasda' )");
c.execute("INSERT INTO NEWS VALUES (7, 'James', 'sda', 'Houston', 10000,'sad','sdasda' )");

