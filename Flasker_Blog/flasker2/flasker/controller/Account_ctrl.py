from flasker.model.User import  User
from flasker.model.Category import Category
import os
from sqlalchemy.exc import IntegrityError
from functools import wraps
from flasker import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,json,jsonify


# -u "un:pwd"
def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/login',methods=['GET','POST'])
def login_check():
    error = None
    if request.method == 'POST':
        rcv_json_dict = request.get_json(silent=True)
        d_username = rcv_json_dict['username']
        d_password = rcv_json_dict['password']
        user = User.query.filter_by(username=d_username).first()
        passwd = User.query.filter_by(password=d_password).first()
        if user is None:
            error = 'Invalid username'
        elif passwd is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return jsonify({'Rep':'Pass'})
    return jsonify({'Rep':'No_Pass'})

@app.route('/User', methods = ['POST','DELETE','PUT'])
@requires_auth
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