from pickle import TRUE
from turtle import color
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    color11='red'
    color22='black'
    return render_template('index.html',rows=8,columns=8,color1=color11,color2=color22)

@app.route('/<int:x>')
def index2(x):
    color11='red'
    color22='black'
    return render_template('index.html',rows=x,columns=8,color1=color11,color2=color22)

@app.route('/<int:x>/<int:y>')
def index3(x,y):
    color11='red'
    color22='black'
    return render_template('index.html',rows=x,columns=y,color1=color11,color2=color22)

@app.route('/<int:x>/<int:y>/<color11>/<color22>')
def index4(x,y,color11,color22):
    return render_template('index.html',rows=x,columns=y,color1=color11,color2=color22)

if __name__=="__main__" :
    app.run(debug=True)
