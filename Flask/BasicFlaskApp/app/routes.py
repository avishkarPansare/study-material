from app import app
from flask import render_template






@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/new_function')
def new_function():
    return "New function "

@app.route('/page_template')
def page_template():
    user = {'username':'Avishkar','fullName':'Avishkar Pansare'}

    return '''
    <html>
        <head>
            <title>
                Home Page - '''+user['fullName']+'''
            </title>
        </head>
        <body>
             <h1> Hello , '''+user['username']+'''!</h1>
        </body>


    </html>
    '''

@app.route('/dynamicTemplateCall')
def dynamicTemplateCall():
    user = {'username':'Avishkar','fullName':'Avishkar Pansare'}
    return render_template('dynamic.html', title='AVISHKAR', user=user)
@app.route('/data')
def data():
    title = "Student"
    user = {'Fname' : 'Avishkar' , 'Lname':'Pansare','username':'AP@gmail.com'}
    students = [
        {
        'name' : 'Omkar',
        'marks': {'Python':'10','Java':'08','C' : '03','DSA':'09'}     
        },
        {
        'name' : 'abhishek',
        'marks': {'Python':'03','Java':'08','C' : '08','DSA':'10'}     
        },
        {
        'name' : 'Sanket',
        'marks': {'Python':'08','Java':'08','C' : '01','DSA':'09'}     
        },
        {
        'name' : 'Pratik',
        'marks': {'Python':'02','Java':'08','C' : '03','DSA':'04'}     
        }
    ]

    return render_template('dynamic.html',title = title , user=user,students=students)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)
  