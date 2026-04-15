# userdao.py

import sqlite3

from user import User

class UserDao():
    """UserDao class - for reading and writing users to and from the database
    
        Please call dao.close() when finished
    """
    def __init__(self, url="C:\\work\\training\\db\\users.db"):
        self.url = url 
        self.conn = sqlite3.connect(self.url)

    def __enter__(self):
        print ("__enter__")
        pass

    def __exit__(self):
        print ("__exit__")
        pass
        
    def get_users(self):
        """return all users from the database"""
        sql = "SELECT * FROM users"
        cur = self.conn.execute(sql)
        # read the whole database in one line!
        users = [User(id, name, email, active) for id, name, email, active in cur]
        return users
    
    def get_user_by_id(self, id_to_find):
        """
        find a user
        
        Params:
        the id to find int

        Returns:
        the user with the specified id

        Raises:
        LookupError if user is not found
        """

        # TODO fix this method
        #raise NotImplementedError("not working")
    

        sql = "SELECT * FROM users WHERE id=?"
        cur = self.conn.execute(sql, (id_to_find,))
        #sql = f"SELECT * FROM users WHERE id={id_to_find}"
        #cur = self.conn.execute(sql)
        record = cur.fetchone()
        if record == None:
            raise LookupError(f"User {id_to_find} not found")

        idd, name, email, active = record
        return User(idd, name, email, active)
    
    def add_user(self, user:User):
        """add a user to the database
        return the newly created user including the automatically assigned id
        NB: user.id is ignored, id will be assigned by the database
        """
        sql = f"""INSERT INTO users
                (name, email, active)
                VALUES(
                    '{user.name}', 
                    '{user.email}', 
                    {1 if user.active else 0})
        """
        cur = self.conn.execute(sql)
        newid = cur.lastrowid if cur.lastrowid else -1

        self.conn.commit()
        return User(newid, user.name, user.email, user.active)

    def delete_user(self, id):
        sql = "DELETE FROM users WHERE id=?"
        self.conn.execute(sql, (id,))
        self.conn.commit()

    def update_user(self, user):
        sql = """UPDATE users
                    SET name=?, email=?, active=?
                WHERE id=?
        """
        self.conn.execute(sql, (user.name, user.email, 1 if user.active else 0, user.id))
        self.conn.commit()
        pass
    def close(self):
        self.conn.close()
        
# Dao
# Data Access Object
# put all db operations into a single class
# someone can use the class
# without knowing anything about the database
if __name__ == "__main__":


    # with UserDao() as dao:

    dao = UserDao()

    #new_user = User(name="New user", email="new.user@gmail.com")
    #added_user = dao.add_user(new_user)

    #print (added_user)

    users = dao.get_users()
    for user in users:
        print (user)

    #id = input("Which user to ?")
    #dao.delete_user(id)

    user_to_update = users[-1]

    user_to_update.name = "Changed"
    user_to_update.email = "changed@gmail.com"
    user_to_update.active = not user_to_update.active

    dao.update_user(user_to_update)

    users = dao.get_users()
    for user in users:
        print (user)

    print ("*" * 50)
    user = dao.get_user_by_id(users[-1].id)

    print (user)

    try:
        user = dao.get_user_by_id(99999)

    except:
        print ("user not found")



    dao.close()



    

