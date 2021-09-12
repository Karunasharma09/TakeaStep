import os
os.chdir(__file__.replace(os.path.basename(__file__),''))
import sqlite3

conn = sqlite3.connect('posts.db', check_same_thread=False)
curr = conn.cursor()

def createtable():
    curr.execute("DROP TABLE IF EXISTS posts")
    curr.execute(""" create table posts ( 
        id integer primary key autoincrement,
        city text ,
        des text ,
        date integer,
        month text,
        year integer,
        area text ) """)
    conn.commit()

def addrow(city , des , date , month , year , area ):
    curr.execute('insert into posts (city , des , date , month , year , area ) values (?,?,?,?,?,?)', (city, des , date , month , year , area ) )
    conn.commit()

def search (city):
    curr.execute('select * from posts where city like ?',("%"+ city +"%",))
    return curr.fetchall()

def deletepost():
    pass

if __name__ == '__main__':
    createtable()
    addrow("guwahati","jdncla;lks,;a",66,"december",8,"bijd")
    v = search("Guwahati")
    print(v)
    var = ("a",)
    print(type(var))
    

