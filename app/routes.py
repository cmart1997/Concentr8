from app import app
from app.counter import *
from flask import Flask, flash, redirect, render_template, request, url_for
from datetime import datetime
import calendar 

@app.route('/')
def index():
    global today, day, month, year
    today = datetime.date(datetime.now())
    today = str(today)
    my_date = datetime.strptime(today, "%Y-%m-%d")
    day = my_date.day
    month = my_date.month
    month = calendar.month_abbr[month]
    year = my_date.year
    return render_template('index.html',day = day, month = month,year = year)

counter = 0 
previous_sessions = {}
@app.route('/click',methods=['GET', 'POST'])
def count():
    global counter
    global previous_session
    if request.method == 'POST':
        counter = counter + 1
    else: 
        if counter != 0: 
            if str(datetime.date(datetime.now())) not in previous_sessions: 
                previous_sessions[today] = []
                    
            else: 
                previous_sessions[today].append(counter)
            
            counter = 0

    return render_template('click.html', counter = counter, previous_sessions = previous_sessions)
