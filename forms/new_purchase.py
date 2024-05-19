from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class NewPurchaseForm(FlaskForm):
    client_id = StringField()
    product_id = StringField()
    store_id = StringField()
    count = StringField()
    submit = SubmitField('Добавить')