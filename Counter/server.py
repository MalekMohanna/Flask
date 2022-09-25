from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'random key for me' 

@app.route('/') 
def homePg():
    if 'num_visits' in session:
        session['num_visits'] += 1
        print('key exists! we are incrementing')
    else:
        session['num_visits'] = 1
    return render_template('count.html')

@app.route('/doubleV', methods = ['POST'])
def doubleVisits():
    session['num_visits'] += 1
    return redirect('/')

@app.route('/incrementV', methods=['POST'])
def manyVisits():
    session['num_visits'] += int(request.form['increasedV'])-1
    return redirect('/')


@app.route("/destroy_session")
def resettingConter():
    session.pop('num_visits') 
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)