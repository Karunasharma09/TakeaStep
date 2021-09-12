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
        area text,
        photo blob ) """)
    conn.commit()

def addrow(city , des , date , month , year , area , photopath ):
    f = open(photopath, 'rb' )
    img = f.read()
    binary = sqlite3.Binary(img)
    curr.execute('insert into posts (city , des , date , month , year , area , photo ) values (?,?,?,?,?,?,?)', (city, des , date , month , year , area , binary) )
    conn.commit()
    f.close()

def search (city):
    curr.execute('select * from posts where city like ?',("%"+ city +"%",))
    result = curr.fetchall()
    # print(result[1][7])
    i = 1
    for img in result:
        f = open(f"temp/images{i}.jpg" , "wb")
        f.write(img[7])
        f.close()
        i += 1
    return result

def deletepost():
    pass

if __name__ == '__main__':
    createtable()
    

