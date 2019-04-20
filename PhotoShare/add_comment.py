from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddCommentForm(FlaskForm):
    CommentText = TextAreaField('Комментарий', validators=[DataRequired()])
    submit = SubmitField('Добавить')

