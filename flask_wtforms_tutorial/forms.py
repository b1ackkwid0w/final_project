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
                string = line.split(", ")
                x = int(string[1])
                y = int(string[2])
                seating_map[x][y] = 'X'
            file.close()
        return seating_map

    def get_reservation_list(self):
        reservation_list = []
        with open("reservations.txt", "r") as file:
            for line in file:
                string = line.split(", ")
                str_dict = {
                    "first_name": string[0],
                    "row": string[1],
                    "seat": string[2],
                    "code": string[3]
                }
                reservation_list.append(str_dict)
            file.close()
        return reservation_list

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

    cost = ReservationCosts()
    seat_price = cost.get_seat_price(cost.matrix, seat)

    res_obj = ReservationList()
    res_list = res_obj.get_reservation_list()
    reservation_num = res_list[len(res_list)-1]['code']

class ReservationCodeStuff():
    recent_reservation_num = "error"

    def writeReservation(self, firstName, row, seat):
        gen_obj = ReservationCodeStuff()
        reservationCode = str(gen_obj.generateReservationCode(firstName))
        reservation = "" + firstName + ", " + str(row) + ", " + str(seat) + ", " + reservationCode + "\n"
        with open('reservations.txt', 'a') as file:
            file.write(reservation)

    def generateReservationCode(self, first_name):
        reservation_num = ""  # initializing reservation number.
        code = "INFOTC1040"  # code for generating the reservation number.

        for i in range(len(first_name)):
            reservation_num += first_name[i]
            reservation_num += code[i]
        reservation_num += code[len(first_name):]
        return reservation_num

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