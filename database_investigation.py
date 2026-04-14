# database_investigation.py

import sqlite3

from user import User

url = "C:\\work\\training\\db\\users.db"
conn = sqlite3.connect(url)


# sql = """INSERT INTO users 
#         (name, email, active) 
#         VALUES('Vicki', 'vicki@gmail.com', 1)"""

# conn.execute(sql)
# conn.commit()


# C.R.U.D
# Create - INSERT
# Retrieve - SELECT
# Update - UPDATE
# Delete - DELETE


#sql = "UPDATE users SET name='changed' WHERE id=8"
#conn.execute(sql)
#conn.commit()

sql = "DELETE FROM users WHERE id = 8"
conn.execute(sql)
conn.commit()


# structured query language
# goal of sql was to create a language that was human readable
sql = "SELECT * FROM users"

cur = conn.execute(sql)

# read the whole database in on line!
users = [User(id, name, email, active) for id, name, email, active in cur]

print (users)



#for id, name, email, active in cur:
#    print (f"{id} {name} {email} {active}")

conn.close()

