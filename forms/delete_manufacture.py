from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class DeleteManufactureForm(FlaskForm):
    manufacturer_id = StringField()
    submit = SubmitField('Удалить')