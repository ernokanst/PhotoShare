from add_photo import AddPhotoForm
from db import DB
from flask import Flask, redirect, render_template, session
from loginform import LoginForm
from photo_model import PhotoModel
from users_model import UsersModel
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jOaqY9515WL6IxQB'
# инициализируем таблицу
db = DB('db.db')
PhotoModel(db.get_connection()).init_table()
UsersModel(db.get_connection()).init_table()
current_page = 'main'


# http://127.0.0.1:8080/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_model = UsersModel(db.get_connection())
        exists = user_model.exists(user_name, password)
        if (exists[0]):
            session['username'] = user_name
            session['user_id'] = exists[1]
        return redirect("/index")
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
def logout():
    session.pop('username', 0)
    session.pop('user_id', 0)
    return redirect('/login')


@app.route('/')
def main():
    current_page = 'main'
    photo = PhotoModel(db.get_connection()).get_all()
    return render_template('main.html', photo=photo)


@app.route('/main')
def redirect_to_main():
    return redirect('/')


@app.route('/index')
def index():
    current_page = 'index'
    if 'username' not in session:
        return redirect('/login')
    photo = PhotoModel(db.get_connection()).get_all(session['user_id'])
    return render_template('index.html', username=session['username'], photo=photo)


@app.route('/add_photo', methods=['GET', 'POST'])
def add_photo():
    if 'username' not in session:
        return redirect('/login')
    form = AddPhotoForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        filename = secure_filename(content.filename)
        if os.path.isfile(os.path.join('static', 'img', filename)):
            while os.path.isfile(os.path.join('static', 'img', filename)):
                filename = filename.split('.')
                filename = '.'.join([filename[0] + 'A', filename[-1]])
        content.save(os.path.join('static', 'img', filename))
        nm = PhotoModel(db.get_connection())
        nm.insert(title, filename, session['user_id'], 0)
        return redirect("/index")
    return render_template('add_photo.html', title='АО МММ', form=form, username=session['username'])


@app.route('/delete_photo/<int:photo_id>', methods=['GET'])
def delete_photo(photo_id):
    if 'username' not in session:
        return redirect('/login')
    nm = PhotoModel(db.get_connection())
    nm.delete(photo_id)
    return redirect("/index")


@app.route('/like_photo/<int:photo_id>', methods=['GET'])
def like_photo(photo_id):
    if 'username' not in session:
        return redirect('/login')
    nm = PhotoModel(db.get_connection())
    nm.likeit(photo_id)
    return redirect("/" + current_page)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
