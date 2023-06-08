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
    cars = models.select_Cars()

    return render_template('search.html', cars = cars)


@app.route('/favourites')
def favourites():

    global currentUser

    cars = []

    if currentUser != 'None':
        cars = models.select_favourites(currentUser)

    return render_template('favourites.html', cars = cars, user = currentUser)

@app.route('/addcar', methods=('GET', 'POST'))
def addcar():
    if request.method == 'POST':
        model = request.form['model']
        german = request.form['German']
        netherlands = request.form['Netherlands']
        unitedKingdom = request.form['UnitedKingdom']
        battery = request.form['Battery']
        acceleration = request.form['Acceleration']
        topSpeed = request.form['TopSpeed']
        range = request.form['Range']
        efficiency = request.form['Efficiency']
        fastCharge = request.form['FastCharge']
        towing = request.form['Towing']
        seats = request.form['Seats']
        cars = models.select_Cars()

        if not model:
            flash('model is required!')
        elif not german:
            flash('german is required!')
        elif not netherlands:
            flash('netherlands is required!')
        elif not unitedKingdom:
            flash('unitedKingdom is required!')
        elif not battery:
            flash('battery is required!')
        elif not acceleration:
            flash('acceleration is required!')
        elif not topSpeed:
            flash('topSpeed is required!')
        elif not range:
            flash('range is required!')
        elif not efficiency:
            flash('efficiency is required!')
        elif not fastCharge:
            flash('fastCharge is required!')
        elif not towing:
            flash('towing is required!')
        elif not seats:
            flash('seats is required!')
        else:
            models.add_car(cars, model, german, netherlands, unitedKingdom, battery, acceleration, topSpeed, range, efficiency, fastCharge, towing, seats)
            return redirect(url_for('index'))

    return render_template('addcar.html')