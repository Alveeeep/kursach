from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class DeleteProductForm(FlaskForm):
    product_id = StringField()
    submit = SubmitField('Удалить')