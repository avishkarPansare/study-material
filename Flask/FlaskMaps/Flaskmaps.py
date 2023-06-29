from flask import Flask ,session,request ,redirect
from flask import Flask, redirect, url_for,render_template
import os
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('roadMap.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001,debug=True)
