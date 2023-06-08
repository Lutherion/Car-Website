from flask import Flask, render_template, request, url_for, flash, redirect
from website import models

from website import app

currentUser = 'None'

@app.route('/')
def index():
    global currentUser
    cars = models.select_Cars()

    return render_template('homepage.html', cars = cars, user = currentUser)

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username:
            flash('Username is required!')
        elif not password:
            flash('Password is required!')
        else:
            user_id = models.select_user_id(username, password)
            if user_id:
                global currentUser
                currentUser = user_id[0][0]
                print(currentUser)
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/favourites')
def favourites():

    global currentUser

    cars = []

    if currentUser != 'None':
        cars = models.select_favourites(currentUser)

    return render_template('favourites.html', cars = cars, user = currentUser)
