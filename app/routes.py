from app import app2 as app
from app.forms import LoginForm
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.models import Post, User

@app.route('/')
@app.route('/index')
def index():
    user1 = {'username': 'Boian'}

    posts = Post.query.all()

    return render_template('index.html', user=user1, posts=posts, title="HelloFlask")

@app.route('/store')
def store():
    items = [
        {
             'title': "Python book",
            'price': 200
        },
        {
            'title': "Cook book",
            'price': 20
        },
        {
            'title': "Samsung Note 5",
            'price': 1000
        },
        {
            'title': "Apartment, monthly",
            'price': 1350
        }
    ]

    return render_template('store.html', items = items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('login'))

    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return "You have been registered"