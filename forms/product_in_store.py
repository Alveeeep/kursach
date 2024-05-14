from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class ProductInStoreForm(FlaskForm):
    product_id = StringField()
    store_id = StringField()
    submit = SubmitField('Найти')