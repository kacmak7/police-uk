import flask
import time

#scripts
import start.py

app = flask.Flask(__name__)

@app.route('/greeting/<username>')
def greet(username):
    return 'hello ' + username

@app.route('/version')
def version():
    return flask.__version__

@app.route('/main')
def main():
    start.do()
    return '! ! ! START SCRIPT HAS STOPPED ! ! !'
