from flask import Flask 
from flask_socketio import SocketIO ,send ,emit
from flask import render_template

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)



@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('msg')
def handleMessage(msg):
    print('Message : '+msg)
    


@socketio.on('userinput')
def handleMessage(name):
    print('Message : '+name)



@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + json['fname'])
    print('received json: ' + json['lname'])
    name = json['fname']+"  "+json['lname']
    socketio.emit('response', name)

if __name__ == '__main__':
    # socketio.run(app,DEBUG=True)
    # socketio.run(app,host='0.0.0.0', port=8001,debug=True)
    socketio.run(app,debug=True)