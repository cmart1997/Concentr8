from app import app
from app.counter import *
from flask import Flask, flash, redirect, render_template, request, url_for

@app.route('/')
def index():
    return render_template('index.html')

counter = 0
@app.route('/click',methods=['GET', 'POST'])
def count():
    global counter
    if request.method == 'POST':
        counter = counter + 1
    
    else: 
        counter = 0
    
    return render_template('click.html', counter = counter)
