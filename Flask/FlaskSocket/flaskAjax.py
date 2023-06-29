from flask import Flask ,session,request ,redirect,jsonify
from flask_socketio import SocketIO ,send ,emit
from flask import render_template
from flask_session import Session
import studentDB
from flask_socketio import join_room, leave_room
import studentDB
from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        name = request.form['name']
        if name == "":
            # return JsonResponse(response_data, safe=False)
            studentData = studentDB.display_student()
            print(studentData[0]['_id'])
            resp = jsonify(success=True,value = name,studentdata=studentData)
            return resp
        

    return render_template('flaskajax.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001,debug=True)