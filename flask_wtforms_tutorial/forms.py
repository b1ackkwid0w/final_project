"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
)

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

class ReservationCosts():
    matrix = [100, 75, 50, 100]

    def get_seat_price(matrix, seat):
        return matrix[seat-1]

    def get_total_sales(matrix):
        # read from reservations.txt
        # extract into array or something and add up matrix[seat-1] for each.
        pass

class ReservationForm(FlaskForm):
    """Reservation Form"""
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
    if reserve:
        cost = ReservationCosts()
        print(cost.matrix)
        price = cost.get_seat_price(seat)
        print(price)

class AdminLoginForm(FlaskForm):
    """Admin login form"""
    
    username = StringField('Username', [DataRequired()])
    password = StringField('Password', [DataRequired()])
    login = SubmitField("Login")