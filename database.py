import os
os.chdir(__file__.replace(os.path.basename(__file__),''))
# import sqlite3
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# conn = sqlite3.connect('posts.db', check_same_thread=False)
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
        photo bytea ) """)
    conn.commit()

def addrow(city , des , date , month , year , area , photopath ):
    f = open(photopath, 'rb' )
    img = f.read()
    binary = psycopg2.Binary(img)
    curr.execute('insert into posts (city , des , date , month , year , area , photo ) values (%s,%s,%s,%s,%s,%s,%s)', (city, des , date , month , year , area , binary) )
    conn.commit()
    f.close()

def search (city):
    curr.execute('select * from posts where city like %s',("%"+ city +"%",))
    result = curr.fetchall()
    # print(result[1][7])
    i = 1
    for img in result:
        f = open(f"static/images{i}.jpg" , "wb")
        f.write(img[7])
        f.close()
        i += 1
    return result

def deletepost():
    pass

if __name__ == '__main__':
    createtable()
    

