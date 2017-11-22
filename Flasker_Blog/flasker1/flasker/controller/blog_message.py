from flasker.model.User import  User
from flasker.model.Category import Category
import os
from sqlalchemy.exc import IntegrityError

from flasker import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

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
    author = session['username']
    category = Category(title,content,author)
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
    #Create request.POST to dedicated response admin_user server 4999
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        headers = {'content-type': 'application/json'}
        url = "http://127.0.0.1:5001/login"
        post_field = {'username':username,'password':password}
        response = requests.post(url, data=json.dumps(post_field), headers=headers)
        ver_dct = response.json()
        if ver_dct['Rep']=='Pass':
            session['logged_in'] = True
            session['username'] = username
            flash('You were logged in')
            return redirect(url_for('show_entries'))

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))