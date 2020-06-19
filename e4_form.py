from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, IntegerField,
                     SubmitField)
from wtforms.validators import InputRequired


class Add(FlaskForm):
    Product_name = StringField('Product_Name')
    amount = IntegerField('Product_amount')
    notes = StringField('Product_notes')
    submit = SubmitField('Add')


class Logging(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('log in')
