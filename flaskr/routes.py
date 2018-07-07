from flaskr import app
from flask import render_template


@app.route('/')
def index():
    posts = [
        {
            'username': "test1",
            'heading': "first",
            'body': "This is the first test"
        },
        {
            'username': "test2",
            'heading': "second",
            'body': "this is the second test"
        }
    ]
    return render_template('index.html', posts=posts)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')
