from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user1 = {'username': 'Boian'}

    posts = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard.'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'body': 'Python can do every thing. However, it is very easy.'
        },
        {
            'title': {'main': 'I love C#', 'sub': 'this is a neutral story'},
            'body': 'C# can do something, and it is very easy.'
        },
        {
            'title': {'main': 'I hate C#', 'sub': 'this is a neutral story'},
            'body': 'C# cannot do anything, and it is stupid!'
        }
    ]

    return render_template('index.html', user = user1, posts = posts)

app.run()
