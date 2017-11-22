from flasker import app

@app.route('/')
def hello_world():
    return 'Welcome to account ctrl page!'

if __name__ == '__main__':
    app.run(port=5001,debug=True)