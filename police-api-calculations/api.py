import flask
import time
from flask import jsonify

#scripts
#import start.py

app = flask.Flask(__name__)

@app.route('/status')
def test():
    return jsonify('OK')

#@app.route('/version')
#def version():
#    return flask.__version__
#
#@app.route('/main')
#def main():
#    start.do()
#    return '! ! ! START SCRIPT HAS STOPPED ! ! !'
