

# class Member():
#     def __init__(self, id, name, email, active):
#         self.id = id
#         self.name = name
#         self.email = email
#         self.active = active
#         pass

#     def __str__(self):
#         return f"{self.id} {self.name} {self.email} {1 if self.active else 0}"
    
from dataclasses import dataclass
from user import User


@dataclass
class Member:
    id: int
    name: str
    email: str
    active: bool


if __name__ == "__main__":
    m = Member(1, "Bob", "bob@gmail.com", True)
    m2 = Member(1, "Bob", "bob@gmail.com", True)
    print (m.name)
    print (m)

    if m == m2:
        print ("members are the same")
    else:
        print ("members are different")

    u = User(1, "Alice", "alice@gmail.com", True)
    u2 = User(1, "Alice", "alice@gmail.com", True)

    if u == u2:
        print ("users are the same")
    else:
        print ("users are different")


