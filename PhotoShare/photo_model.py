class PhotoModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS photo 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                 title VARCHAR(100),
                                 content VARCHAR(1000),
                                 user_id INTEGER,
                                 likes INTEGER,
                                 comments VARCHAR(10000)
                                 )''')
        cursor.close()
        self.connection.commit()

    def insert(self, title, content, user_id, likes):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO photo 
                          (title, content, user_id, likes, comments) 
                          VALUES (?,?,?,?,?)''', (title, content, str(user_id),
                                                  str(likes), ''))
        cursor.close()
        self.connection.commit()

    def get(self, photo_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM photo WHERE id = ?", (str(photo_id),))
        row = cursor.fetchone()
        return row

    def get_all(self, user_id=None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute(
                "SELECT * FROM photo WHERE user_id = ?", (str(user_id),))
        else:
            cursor.execute("SELECT * FROM photo")
        rows = cursor.fetchall()
        return rows

    def delete(self, photo_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM photo WHERE id = ?''',
                       (str(photo_id),))
        cursor.close()
        self.connection.commit()

    def likeit(self, photo_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT likes FROM photo WHERE id = ?",
                       (str(photo_id),))
        like_count = int(cursor.fetchone()[0] + 1)
        cursor.execute('''UPDATE photo SET likes = ? WHERE id = ?''',
                       (str(like_count), str(photo_id)))
        cursor.close()
        self.connection.commit()
