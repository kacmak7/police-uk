import flask
import time

app = flask.Flask(__name__)

@app.route('/greeting/<username>')
def greet(username):
    return 'hello ' + username

@app.route('/version')
def version():
    return flask.__version__

@app.route('/main')
def main():
    
    return 'executed'
