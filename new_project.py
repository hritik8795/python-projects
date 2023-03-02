import sqlite3
db =sqlite3.connect("new.db")
cr =db.cursor()
r =cr.execute("create table regis(UNAME text, UPASS text, UCN text)")
#r =cr.execute("create table ins(UROLLNO text,UNAME text, Uphy text, Uche text,UMATH text)")
db.commit()
db.close()
print("data inserted")