from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class AddManufactureForm(FlaskForm):
    name = StringField()
    submit = SubmitField('Добавить')