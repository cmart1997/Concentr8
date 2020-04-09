from app import app
from flask import render_template

@app.route('/')
def index():
    count = 0 
    print(count)
    return render_template('index.html',count = count)

@app.route('/#')
def count():
    count += 1
    return render_template('index.html',count = count)

