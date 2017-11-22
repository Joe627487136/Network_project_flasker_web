# Flasker Blog #
## Before running the server ##
- a. Direct to your project directory in your terminal eg: cd /Users/blablabla/PycharmProjects/Flasker_Blog(Project name)/flakser1(Firser Server)


- b. Please install python SQLAlCHEMY environment, if there is no such environment then please install by command line: 

```
    pip install SQLAlchemy
```

- c. Then enter python enironment by key "python" in terminal


- d. Create related database by python:
```
    from flasker import db

    db.create_all()
```

- e. Under "Flasker1" directory to setting.py, Please implement your own database access info:
```
    eg:

    SQLALCHEMY_DATABASE_URI = "mysql://root:your_db_password@127.0.0.1:3306/Flasker_DB"**

    "mysql://your server name:your password@your server ip:port number/DB name"**
```

Then you can also refer to below screenshot if you have any problems during setup.
If you have encounter error of missing library package, please install before you create the database.
<p align="center">
<img src="https://github.com/Joe627487136/flasker_lab1/blob/master/Setup_Screenshot/Screenshot%202017-09-26%2015.10.17.png" width="480" align="center">
</p>

- f. Code structure:
```
.../Flasker_Blog
├── flasker1
│   ├── flasker
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   └── setting.cpython-36.pyc
│   │   ├── controller
│   │   │   ├── __pycache__
│   │   │   │   └── blog_message.cpython-36.pyc
│   │   │   └── blog_message.py
│   │   ├── model
│   │   │   ├── Category.py
│   │   │   ├── User.py
│   │   │   └── __pycache__
│   │   │       ├── Category.cpython-36.pyc
│   │   │       └── User.cpython-36.pyc
│   │   ├── setting.py
│   │   ├── static
│   │   │   └── style.css
│   │   └── templates
│   │       ├── layout.html
│   │       ├── login.html
│   │       └── show_entries.html
│   └── runserver.py
└── flasker2
    ├── flasker
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   └── setting.cpython-36.pyc
    │   ├── controller
    │   │   ├── Account_ctrl.py
    │   │   └── __pycache__
    │   │       └── Account_ctrl.cpython-36.pyc
    │   ├── model
    │   │   ├── Category.py
    │   │   ├── User.py
    │   │   └── __pycache__
    │   │       ├── Category.cpython-36.pyc
    │   │       └── User.cpython-36.pyc
    │   ├── setting.py
    │   ├── static
    │   └── templates
    └── runserver.py


```

- g. Create your own admin account on Server 2:
```
Direct to .../Flasker_Blog(Project name)/flakser2(Firser Server)/flask/controller/Account_ctrl.py
Then in check_auth func you can modify your admin account and password, default:(admin,secret)
```
## How to run the server?

### Introduce to system structure ###
<p align="center">
<img src="https://github.com/Joe627487136/Network_project_flasker_web/blob/master/Setup_Screenshot/Flasker_Struct.png" width="480" align="center">
</p>

User can only access server 1 and server 1 will respond to db to achieve the basic blog function query (eg: blog posts)
User login will generate post request to server 1 and after server 1 receive the post request it will generate its own post request to query the account server which can access and check the sensitive user info data in db.


## After the server is running ##

### Down below are several curl commands which can implement to create your user without using MySQL commands: ###

#### Create user(username="Teckwu3", password="teck123") ("POST"):
curl -H "Content-type: application/json" \ -X POST http://127.0.0.1:5001/User -d '{"username":"Teck1234", "password":"Teck1234"}' -u "admin:secret"

#### Update user with new password (username="Teckwu3", old password="teck123", new password="teck") ("PUT"):
curl -H "Content-type: application/json"  -X PUT http://127.0.0.1:5001/User -d '{"username":"Teck1234", "password":"Teck1234", "newpassword":"teck"}' -u "admin:secret"

#### Delete user(username="Teckwu3", password="teck") ("DELETE"):
curl -H "Content-type: application/json" \ -X POST http://127.0.0.1:5001/User -d '{"username":"Teck1234", "password":"teck"}' -u "admin:secret"
