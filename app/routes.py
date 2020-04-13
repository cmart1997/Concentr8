from app import app
from app.counter import *
from flask import Flask, flash, redirect, render_template, request, url_for
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

counter = 0 
previous_sessions = {}
@app.route('/click',methods=['GET', 'POST'])
def count():
    global counter
    global previous_session
    if request.method == 'POST':
        counter = counter + 1
    else: 
        today = datetime.date(datetime.now())
        today = str(today)
        if str(datetime.date(datetime.now())) not in previous_sessions: 
            previous_sessions[today] = []
            
        else: 
            previous_sessions[today].append(counter)
        
        counter = 0

    return render_template('click.html', counter = counter, previous_sessions = previous_sessions)
