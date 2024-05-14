from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class ClientEditForm(FlaskForm):
    email = EmailField()
    phone = TelField()
    firstname = StringField()
    lastname = StringField()
    submit = SubmitField('Сохранить')
