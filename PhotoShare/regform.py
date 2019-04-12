from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename


class RegForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repassword = PasswordField(
        'Повторите пароль', validators=[DataRequired()])
    content = FileField('Аватар', validators=[
                        FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Зарегистрироваться')
