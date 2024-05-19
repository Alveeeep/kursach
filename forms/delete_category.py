from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TelField, EmailField


class DeleteCategoryForm(FlaskForm):
    category_id = StringField()
    submit = SubmitField('Удалить')