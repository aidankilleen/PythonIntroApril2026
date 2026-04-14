# user.py

class User():
    def __init__(self, id=-1, name="", email="", active=False):
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        
    def __str__(self):
        #    inline conditional
        # print ("__str__() called")
        return f"{self.id} {self.name} {self.email} {"Active" if self.active else "Inactive"}"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":

    users = [User(1, "Alice", "alice@gmail.com", True), 
             User(2, "Bob", "bob@gmail.com", False), 
             User(3, "Carol", "carol@gmail.com", True),
             User(4, "Dan", "dan@gmail.com", True),
             User(5, "Eve", "eve@gmail.com", False)]
    
    str(users[0])

    exit(0)


    for user in users:
        print (user)

    print ("*" * 50)

    active_users = [user for user in users if user.active]

    print (active_users)


    # non pythonic way
    # for user in users:
    #     if user.active:
    #         active_users.append(user)











    u = User(1, "Alice", "alice@gmail.com", True)
    u2 = User(name="Bob")


    print (u)
    print (u2)
