from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class StoreSearchForm(FlaskForm):
    store_id = StringField()
    submit = SubmitField('Найти')