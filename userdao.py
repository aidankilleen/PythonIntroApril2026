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
# Dao
# Data Access Object
# put all db operations into a single class
# someone can use the class
# without knowing anything about the database
if __name__ == "__main__":

    dao = UserDao()

    users = dao.get_users()
    for user in users:
        print (user)





    

