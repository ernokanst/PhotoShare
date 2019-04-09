from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename


class AddPhotoForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = FileField('Фото', validators=[
                        FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Добавить')

