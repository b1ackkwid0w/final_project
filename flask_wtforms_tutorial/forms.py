"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
)
#from datetime import date
#from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class UserOptionForm(FlaskForm):
    """Generate Your Graph."""
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    option = SelectField("Choose an Option",[DataRequired()],
        choices=[
            ("", "Choose an option"),
            ("1", "Admin Login"),
            ("2", "Reserve a seat"),
        ],
    )

    submit = SubmitField("Submit")

class ReservationCosts():
    matrix = [100, 75, 50, 100]

    def get_seat_price(self, matrix, seat):
        print(type(seat))
        # return int(matrix[int(seat)-1])

    def get_total_sales(self, matrix):
        salesFile = open('reservations.txt', 'r')
        listOfSales = []
        
        for line in salesFile:
            strippedLine = line.strip()
            lineList = strippedLine.split(", ")
            seatNum = lineList[2]
            seatCost = matrix[int(seatNum)-1]
            listOfSales.append(seatCost)

        salesFile.close()    

        totalCost = sum(listOfSales)
        return totalCost

class ReservationForm(FlaskForm):
    """Reservation Form"""
    
    seating_map = [['O']*4 for row in range(12)]
    with open("reservations.txt", "r") as file:
        for line in file:
            string = line.split(",")
            x = int(string[1])
            y = int(string[2])
            seating_map[x][y] = 'X'
        file.close()
    seating_chart = seating_map


    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [DataRequired()])
    row = SelectField("Choose Row", [DataRequired()],
        choices=[
            ("", "Choose a Row"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
        ],
    )
    seat = SelectField("Choose Seat", [DataRequired()],
        choices=[
            ("", "Choose a Seat"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
        ],
    )

    reserve = SubmitField("Reserve a Seat")
    if reserve is True:
        cost = ReservationCosts()
        # print(cost.matrix)
        price = cost.get_seat_price(cost.matrix, seat)
        # print(price)
 

    # seating_map = [['O']*4 for row in range(12)]
    # with open("reservations.txt", "r") as file:
    #     for line in file:
    #         string = line.split(",")
    #         x = int(string[1])
    #         y = int(string[2])
    #         seating_map[x][y] = 'X'
    #     file.close()
    # seating_chart = seating_map

    
        

class AdminLoginForm(FlaskForm):
    """Admin login form"""
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    username = StringField('Username', [DataRequired()])
    password = StringField('Password', [DataRequired()])
    login = SubmitField("Login")
    if login is True:

        # get total sales
        cost = ReservationCosts()
        total = cost.get_total_sales(cost.matrix)
        # print(total)

        seating_map = [['O']*4 for row in range(12)]
        with open("reservations.txt", "r") as file:
            for line in file:
                string = line.split(",")
                x = int(string[1])
                y = int(string[2])
                seating_map[x][y] = 'X'
            file.close()
        seating_chart = seating_map
    else:
        seating_chart = ''