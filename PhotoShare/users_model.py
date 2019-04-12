class UsersModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password_hash VARCHAR(128),
                             content VARCHAR(1000)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash, content):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash, content) 
                          VALUES (?,?,?)''', (user_name, password_hash, content))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE user_name = ? AND password_hash = ?", (user_name, password_hash))
        row = cursor.fetchone()
        return (True, row) if row else (False,)

    def login_used(self, user_name):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE user_name = ?", (user_name,))
        row = cursor.fetchone()
        return True if row else False
