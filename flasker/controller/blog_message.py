from flasker.model.User import  User
from flasker.model.Category import Category
import os
from sqlalchemy.exc import IntegrityError

from flasker import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,json

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

@app.route('/')
def show_entries():
    categorys = Category.query.all()
    return render_template('show_entries.html',entries=categorys)

@app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = request.form['title']
    content = request.form['text']
    category = Category(title,content)
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=request.form['username']).first()
        passwd = User.query.filter_by(password=request.form['password']).first()

        if user is None:
            error = 'Invalid username'
        elif passwd is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/User', methods = ['POST','DELETE','PUT'])
def api_user():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            try:
                JSON_Datalist = json.dumps(request.json)
                mydict = json.loads(JSON_Datalist)
                print(mydict)
                user_name = mydict['username']
                pwd = mydict['password']
                user = User(user_name, pwd)
                db.session.add(user)
                db.session.commit()
                return "New user registered: " + json.dumps(request.json) + "\n"
            except KeyError:
                return "Unmatched Format! JSON Message must be {\"username\":\"your_username\",\"password\":\"your_password\"}!\n"
            except IntegrityError:
                return "This username is already taken by someone else! Please choose another username!\n"
        else:
            return "415 Unsupported Type ;)"

    elif request.method == 'PUT':
        if request.headers['Content-Type'] == 'application/json':
            try:
                JSON_Datalist = json.dumps(request.json)
                mydict = json.loads(JSON_Datalist)
                print(mydict)
                current_user_name = mydict['username']
                current_pwd = mydict['password']
                new_pwd = mydict['newpassword']
                our_user = db.session.query(User).filter_by(username=current_user_name).first()
                if(our_user == None):
                    return "Please input a valid username!\n"
                if(our_user.password == current_pwd):
                    our_user.password = new_pwd
                    db.session.commit()
                    return "Committed change: "+ json.dumps(request.json) + "\n"
                if(our_user.password != current_pwd):
                    return "Please input a valid password!\n"
            except KeyError:
                return "Unmatched Format! JSON Message must be {\"username\":\"your_username\",\"password\":\"your_password\",\"newpassword\":\"your_newpassword\"}!\n"
            except IntegrityError:
                return "Please pick valid username!\n"
            else:
                return "415 Unsupported Type ;)"

    elif request.method == 'DELETE':
        if request.headers['Content-Type'] == 'application/json':
            try:
                JSON_Datalist = json.dumps(request.json)
                mydict = json.loads(JSON_Datalist)
                print(mydict)
                current_user_name = mydict['username']
                current_pwd = mydict['password']
                our_user = db.session.query(User).filter_by(username=current_user_name).first()
                if(our_user == None):
                    return "Please input a valid username!\n"
                if(our_user.password == current_pwd):
                    db.session.delete(our_user)
                    db.session.commit()
                    return "Committed change: "+ json.dumps(request.json) + "\n"
            except KeyError:
                return "Unmatched Format! JSON Message must be {\"username\":\"your_username\",\"password\":\"your_password\"}!\n"
            except IntegrityError:
                return "Please pick valid username!\n"
            else:
                return "415 Unsupported Type ;)"