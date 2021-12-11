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
    
    option = SelectField("Choose an Option",[DataRequired()],
        choices=[
            ("", "Choose an option"),
            ("1", "Admin Login"),
            ("2", "Reserve a seat"),
        ],
    )

    submit = SubmitField("Submit")

class ReservationList():
    def get_seating_chart(self):
        seating_map = [['O']*4 for row in range(12)]
        with open("reservations.txt", "r") as file:
            for line in file:
                string = line.split(",")
                x = int(string[1])
                y = int(string[2])
                seating_map[x][y] = 'X'
            file.close()
        return seating_map

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
    
    reservation_list = ReservationList()
    seating_chart = reservation_list.get_seating_chart()

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
        price = cost.get_seat_price(cost.matrix, seat)

# class UserLoginInfo():
#     def get_user_login():
#         userLoginFile = open('passcodes.txt', 'r')
#         userLoginList = []
        
#         for line in salesFile:
#             strippedLine = line.strip()
#             lineList = strippedLine.split(", ")
#             seatNum = lineList[2]
#             seatCost = matrix[int(seatNum)-1]
#             listOfSales.append(seatCost)

#         salesFile.close()    

#         totalCost = sum(listOfSales)
#         return totalCost

class AdminLoginForm(FlaskForm):
    """Admin login form"""
    
    username = StringField('Username', [DataRequired()])
    password = StringField('Password', [DataRequired()])
    login = SubmitField("Login")

    reservation_list = ReservationList()
    seating_chart = reservation_list.get_seating_chart()
        # with open ('passcodes.txt', 'r') as file:
        #     reader = csv.reader(file, delimiter=",")
        #     for row in reader: 
        #         if (request.form['username'] == 'admin1' and request.form['password'] == '12345'):
        #             return redirect('reservations')

        # userLoginList = []
        # with open ('passcodes.txt', 'r') as file:
        #     reader = csv.reader(file, delimiter=", ")
        #     for row in reader: 
        #         row[1] = row[1].strip()
        #         userInfo.append(row)

        # if request.method == 'POST' and form.validate_on_submit():
        #     for user in userInfo:
        #         if (request.form['username'] == user[0] and request.form['password'] == user[1]):
        #             pass    # return redirect('reservations')
        #             # Redirected for testing purposes
        #             # We need to show the reservation table right here
        #             # But I can't get anything to print in the form

    cost = ReservationCosts()
    total_sales = cost.get_total_sales(cost.matrix)