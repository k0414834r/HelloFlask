from app import app2 as app
from app.forms import LoginForm
from flask import Flask, render_template, flash, redirect

from app import Post

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect('/login')

    return render_template('login.html', title = 'Sign In', form = form)