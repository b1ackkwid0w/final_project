from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

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
    
    # with open ('passcodes.txt', 'r') as file:
    #         reader = csv.reader(file, delimiter=",")
    #         for row in reader: 
    #             if (request.form['username'] == 'admin1' and request.form['password'] == '12345'):
    #                 return redirect('reservations')
    userInfo = getUserInfo()

    form = AdminLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        for user in userInfo:
                if (request.form['username'] == user[0] and request.form['password'] == user[1]):
                    return redirect('reservations')
                    # Redirected for testing purposes
                    # We need to show the reservation table right here
                    # But I can't get anything to print in the form

    


    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

def getUserInfo():
     userInfo = []
     with open ('passcodes.txt', 'r') as file:
          reader = csv.reader(file, delimiter=",")
          for row in reader: 
               row[1] = row[1].strip()
               userInfo.append(row)
     return userInfo