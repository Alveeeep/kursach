from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class ProductEditForm(FlaskForm):
    name = StringField()
    manufacture_id = StringField()
    category_id = StringField()
    price = StringField()
    submit = SubmitField('Сохранить')