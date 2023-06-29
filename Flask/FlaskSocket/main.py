from flask import Flask ,session,request ,redirect
from flask_socketio import SocketIO ,send ,emit
from flask import render_template
from flask_session import Session
import studentDB
from flask_socketio import join_room, leave_room
from werkzeug.utils import secure_filename
import pandas as pd
from flask import Flask, redirect, url_for
import os
app = Flask(__name__)
# UPLOAD_FOLDER = '/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FO
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER']= './uploads'
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)



@app.route('/')
def index():
    return render_template('indexStudent.html')


@socketio.on('msg')
def handleMessage(msg):
    print('Message : '+msg)
    


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



@socketio.on("student_rec")
def student_page(data):
    print(data)
    studentData = studentDB.display_student()

    socketio.emit('StudentData', studentData)


@socketio.on("student_getData")
def student_getData(data):
    print(data)
    studentData = studentDB.student_getDataId(data)
    socketio.emit('StudentDataID', studentData)

@socketio.on("studentUpdateId")
def studentUpdateId(data):
    print(data)
    studentData = studentDB.studentUpdateId(data)
    socketio.emit('Student_UpdateID', studentData)

@socketio.on("studentinsert")
def studentinsert(data):
    studentData = studentDB.studentinsert(data)
    socketio.emit('StudentData', studentData)


@app.route('/StudentData', methods=['POST'])
def StudentData():
    if request.method == "POST":
        name = request.form['_id']
        print(name)

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       df= pd.read_csv(f.filename)
#       print(df)
#
#       # f.save(secure_filename(f.filename))
#       df_lst = df.to_dict('records')
#       print(df_lst)
#       studentData = studentDB.studentInsertMany(df_lst)
#       filename = secure_filename(f.filename)
#       f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#
#       # # return redirect(url_for('/'))
#       return render_template('indexStudent.html')
#       # return 'file uploaded successfully'


@app.route('/uploader', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    df = pd.read_csv(uploaded_file.filename)
    df_lst = df.to_dict('records')
    print(df_lst)
    studentData = studentDB.studentInsertMany(df_lst)
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))





if __name__ == '__main__':
    # socketio.run(app,DEBUG=True)
    socketio.run(app,host='0.0.0.0', port=8001,debug=True)

    # socketio.run(app,debug=True)