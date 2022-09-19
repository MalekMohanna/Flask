from flask import Flask, render_template,request,session,redirect
app= Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def info():
    session['user_name'] = request.form['name']
    session['user_location']= request.form['location']
    session['user_language'] = request.form['Language']
    session['user_comment'] = request.form['comment']
    session['user_os']=request.form['OS']
    session['user_answer']=request.form['answer']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)