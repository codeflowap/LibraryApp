import sqlite3

def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER  PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows
    
connect()
insert("Statistical Learning", "J. Hastie", 2012, 88987632)
insert("Machile and AI" , "A. Chalres", 2012, 88987632)
print(rows)
