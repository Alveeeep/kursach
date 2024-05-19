from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class AddCategoryForm(FlaskForm):
    name = StringField()
    submit = SubmitField('Добавить')