class CommentModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS comment 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                 user_name VARCHAR(100),
                                 photo_id INTEGER,
                                 commentText VARCHAR(10000)
                                 )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, photo_id, commentText):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO comment 
                          (user_name, photo_id, commentText) 
                          VALUES (?,?,?)''', (user_name, str(photo_id),
                                              commentText))
        cursor.close()
        self.connection.commit()

    def get(self, photo_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM comment WHERE photo_id = ?", (str(photo_id),))
        row = cursor.fetchall()
        return row

    def delete(self, comment_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM comment WHERE id = ?''',
                       (str(comment_id),))
        cursor.close()
        self.connection.commit()
