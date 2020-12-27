from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lyor'}
    posts = [
        {
            'author': {'username': 'Bobby'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Molly'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Eric'},
            'body': 'Screw you guys i\'m going home'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)