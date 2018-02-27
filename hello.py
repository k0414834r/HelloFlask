from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user1 = {'username': 'Boian'}

    posts = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'price': 'Python can do every thing. However, it is very hard.'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'price': 'Python can do every thing. However, it is very easy.'
        },
        {
            'title': {'main': 'I love C#', 'sub': 'this is a neutral story'},
            'price': 'C# can do something, and it is very easy.'
        },
        {
            'title': {'main': 'I hate C#', 'sub': 'this is a neutral story'},
            'price': 'C# cannot do anything, and it is stupid!'
        }
    ]

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

app.run()
