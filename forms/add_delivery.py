from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField, DateField


class AddDeliveryForm(FlaskForm):
    product_id = StringField()
    store_id = StringField()
    delivery_date = DateField()
    count = StringField()
    submit = SubmitField('Добавить')