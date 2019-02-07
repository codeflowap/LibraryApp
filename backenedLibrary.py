import sqlite3

def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER  PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
    
connect()
