# Flasker Blog #
## Before running the server ##
- a. Direct to your project directory in your terminal eg: cd /Users/zhouxuexuan/PycharmProjects/Flasker_Blog(Project name)/flakser1(Firser Server)


- b. Please install python SQLAlCHEMY environment, if there is no such environment then please install by command line: 


    >**pip install SQLAlchemy**


- c. Then enter python enironment by key "python" in terminal


- d. Create related database by python:

    >from flasker import db

    >db.create_all()


- e. Under "Flasker1" directory to setting.py, Please implement your own database access info:

    >eg:

    >**SQLALCHEMY_DATABASE_URI = "mysql://root:your_db_password@127.0.0.1:3306/Flasker_DB"**

    >**"mysql://your server name:your password@your server ip:port number/DB name"**


Then you can also refer to below screenshot if you have any problems during setup.
If you have encounter error of missing library package, please install before you create the database.
<img src="https://github.com/Joe627487136/flasker_lab1/blob/master/Setup_Screenshot/Screenshot%202017-09-26%2015.10.17.png" width="480" align="center">

- f. Code structure:

  Flasker_Blog <br />
  ├── flasker1 [(Blog Server)](https://github.com/Joe627487136/Network_project_flasker_web/tree/master/Flask_Blog/flasker1) <br />
  │   ├── flasker <br />
  │   │   ├── __init__.py <br />
  │   │   ├── __pycache__ <br />
  │   │   │   ├── __init__.cpython-36.pyc <br />
  │   │   │   └── setting.cpython-36.pyc <br />
  │   │   ├── controller <br />
  │   │   │   ├── __pycache__ <br />
  │   │   │   │   └── blog_message.cpython-36.pyc <br />
  │   │   │   └── blog_message.py <br />
  │   │   ├── model <br />
  │   │   │   ├── Category.py <br />
  │   │   │   ├── User.py <br />
  │   │   │   └── __pycache__ <br />
  │   │   │       ├── Category.cpython-36.pyc <br />
  │   │   │       └── User.cpython-36.pyc <br />
  │   │   ├── setting.py <br />
  │   │   ├── static <br />
  │   │   │   └── style.css <br />
  │   │   └── templates <br />
  │   │       ├── layout.html <br />
  │   │       ├── login.html <br />
  │   │       └── show_entries.html <br />
  │   └── runserver.py <br />
  └── flasker2 [(Admin Server)](https://github.com/Joe627487136/Network_project_flasker_web/tree/master/Flask_Blog/flasker2) <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── flasker <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│   ├── __init__.py <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│   ├── __pycache__ <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   ├── __init__.cpython-36.pyc <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   └── setting.cpython-36.pyc <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── controller <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   ├── Account_ctrl.py <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   └── __pycache__ <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │       └── Account_ctrl.cpython-36.pyc <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── model <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   ├── Category.py <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   ├── User.py <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   └── __pycache__ <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │       ├── Category.cpython-36.pyc <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │       └── User.cpython-36.pyc <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── setting.py <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── static <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   └── templates <br />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    └── runserver.py <br />

    
    
## How to run the server?

### Introduce to system structure ###
![Alt text](https://github.com/Joe627487136/Network_project_flasker_web/blob/master/Setup_Screenshot/Flasker_Struct.png?raw=true "Title")

User can only access server 1 and server 1 will respond to db to achieve the basic blog function query (eg: blog posts)
User login will generate post request to server 1 and after server 1 receive the post request it will generate its own post request to query the account server which can access and check the sensitive user info data in db.


## After the server is running ##

### Down below are several curl commands which can implement to create your user without using MySQL commands: ###

#### Create user(username="Teckwu3", password="teck123") ("POST"):
curl -H "Content-type: application/json" \ -X POST http://127.0.0.1:5000/User -d '{"username":"Teckwu3", "password":"teck123"}'

#### Update user with new password (username="Teckwu3", old password="teck123", new password="teck") ("PUT"):
curl -H "Content-type: application/json" \ -X PUT http://127.0.0.1:5000/User -d '{"username":"Teckwu3", "password":"teck123", "newpassword";"teck"}'

#### Delete user(username="Teckwu3", password="teck") ("DELETE"):
curl -H "Content-type: application/json" \ -X POST http://127.0.0.1:5000/User -d '{"username":"Teckwu3", "password":"teck"}'
