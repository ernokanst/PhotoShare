from add_news import AddNewsForm
from db import DB
from loginform import LoginForm
from news_model import NewsModel
from users_model import UsersModel


#инициализируем таблицу
db = DB('db.db')
UsersModel(db.get_connection()).init_table()
user_ = UsersModel(db.get_connection())
#добавляем пользователя (по одному!!!!!)
user_.insert('Admin','pass')

