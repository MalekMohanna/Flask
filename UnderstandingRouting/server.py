from flask import Flask

app = Flask(__name__) 
@app.route('/') 
def say_hello():     
    return 'Hello world'  
@app.route('/dojo') 
def dojo():     
    return 'Dojo!'  
@app.route('/say/<name>') 
def say_name(name):     
        return 'Hi '+ name  
@app.route('/repeat/<int:repeat>/<text>') 
def repeat(repeat,text):     
    return text*repeat
@app.errorhandler(404) 
def wrong(e):     
    return 'Sorry! No response. Try again.'  
if __name__ == "__main__":     
    app.run(debug=True)