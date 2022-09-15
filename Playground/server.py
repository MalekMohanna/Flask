from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index(case=0):
    return render_template("index.html",mycase=case)

@app.route('/play/<int:x>')
def page2(x,case=2):
    return render_template('index.html',repeat=x,mycase=case)

@app.route('/play/<int:x>/<color>')
def page3(x,color,case=3):
    return render_template('index.html',repeat=x,mycolor=color,mycase=case)

if __name__=="__main__":
    app.run(debug=True)