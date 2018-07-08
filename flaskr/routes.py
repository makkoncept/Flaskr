from flaskr import app
from flask import render_template, redirect, url_for, flash
from flaskr.forms import LoginForm, RegisterForm


@app.route('/')
def home():
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


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"{form.username.data} Successfully logged in")
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if register.validate_on_submit():
        flash(f'{register.username.data}, registered')
        return redirect(url_for('login'))
    return render_template('register.html', register=register)
