from flask import Flask ,session,request ,redirect
from flask_socketio import SocketIO ,send ,emit
from flask import render_template
from flask_session import Session

from flask_socketio import join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)



@app.route('/')
def index():
    return render_template('index1.html')


# @socketio.on('msg')
# def handleMessage(msg):
#     print('Message : '+msg)
    


# @socketio.on('userinput')
# def handleMessage(name):
#     print('Message : '+name)



@socketio.on('Gmsg')
def handle_msg(data):
    print(session.get(data['room']))
    if session.get(data['room']):
        print('received json: ' + data['msg'])
        print('received json: ' + data['room'])


        socketio.emit('avishkar',data)




@socketio.on('join')
def on_join(data):
    if not session:
        session[data['room']] = data['room']
        print("Room Name ",data['room'])
        room = data['room']
        join_room(room)
        data = {'room':room}
        socketio.emit('RoomName',data )



@socketio.on('leave')
def on_leave(data):

    if session.get(data['room']):
        room = data['room']
        leave_room(room)
        session[data['room']] = None
        # return render_template('index1.html')












if __name__ == '__main__':
    # socketio.run(app,DEBUG=True)
    socketio.run(app,host='0.0.0.0', port=8001,debug=True)
    # socketio.run(app,debug=True)