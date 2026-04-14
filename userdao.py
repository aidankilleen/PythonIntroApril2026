# userdao.py

import sqlite3

from user import User

class UserDao():
    def __init__(self, url="C:\\work\\training\\db\\users.db"):
        self.url = url 
        self.conn = sqlite3.connect(self.url)
        
    def get_users(self):
        sql = "SELECT * FROM users"
        cur = self.conn.execute(sql)
        # read the whole database in one line!
        users = [User(id, name, email, active) for id, name, email, active in cur]
        return users
    
    def add_user(self, user:User):
        sql = f"""INSERT INTO users
                (name, email, active)
                VALUES(
                    '{user.name}', 
                    '{user.email}', 
                    {1 if user.active else 0})
        """
        self.conn.execute(sql)
        pass
# Dao
# Data Access Object
# put all db operations into a single class
# someone can use the class
# without knowing anything about the database
if __name__ == "__main__":

    dao = UserDao()

    new_user = User(name="New user", email="new.user@gmail.com")
    dao.add_user(new_user)

    users = dao.get_users()
    for user in users:
        print (user)





    

