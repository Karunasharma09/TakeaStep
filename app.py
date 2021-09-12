from flask import Flask, render_template , request;
import os
import database
import datetime
os.chdir(__file__.replace(os.path.basename(__file__),''))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def web1():
    city = request.args['citysearch']
    view = database.search(city)
    
    return render_template('search.html',cityname = city,posts = view , n=len(view))

@app.route('/post', methods = ['POST'])
def web2():
    city = request.form['city']
    area = request.form['area']
    des = request.form['des']
    image = request.files['image']
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'temp/upload.jpg'))
    x = datetime.datetime.now()
    database.addrow(city,des,x.strftime("%d"),x.strftime("%B"),x.strftime("%Y"),area, 'temp/upload.jpg' )

    return render_template('post.html',city = city,des = des,area = area)

if __name__ == '__main__':
    app.run()
