from flask import Flask ,session,request ,redirect,jsonify
from flask_socketio import SocketIO ,send ,emit
from flask import render_template
from flask_session import Session

from flask import Flask
import pygal
from pygal.style import Style

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bar.html')







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001,debug=True)