from os import write
from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash, jsonify

from .forms import *

import csv

#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    userInfo = getUserInfo()
    form = AdminLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        for user in userInfo:
                if (request.form['username'] == user[0] and request.form['password'] == user[1]):
                    return render_template("admin.html", form=form, template="form-template")
                else:
                    return redirect('/')
                    # Redirected for testing purposes
                    # We need to show the reservation table right here
                    # But I can't get anything to print in the form


    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    
    reservedSeats = getReservedSeats()

    form = ReservationForm()

    if request.method == 'POST' and form.validate_on_submit:
        selectedRow = int(request.form['row'].strip()) - 1
        selectedSeat = int(request.form['seat'].strip()) - 1
        firstName = str(request.form['first_name'])

        res_code_obj = ReservationCodeStuff()

        if reservedSeats[selectedRow][selectedSeat] == False:
            res_code_obj.writeReservation(firstName, selectedRow, selectedSeat)
            res_code_obj.recent_reservation_num = res_code_obj.generateReservationCode(firstName)
            reservedSeats[selectedRow][selectedSeat] = True

    return render_template("reservations.html", form=form, template="form-template")

def getUserInfo():
    userInfo = []
    with open ('passcodes.txt', 'r') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader: 
            row[1] = row[1].strip()
            userInfo.append(row)
    return userInfo

def getReservedSeats():
    reservedSeats = []
    i = 0
    while i < 12:
        reservedSeats.append({0: False, 1: False, 2: False, 3: False})
        i += 1

    with open ('reservations.txt', 'r') as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            currentRow = int(row[1].strip())
            currentSeat = int(row[2].strip())
            
            if reservedSeats[currentRow][currentSeat] == False:
                reservedSeats[currentRow][currentSeat] = True

    return reservedSeats
