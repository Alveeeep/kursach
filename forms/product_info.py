from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class ProductInfotForm(FlaskForm):
    product_id = StringField()
    submit = SubmitField('Найти')