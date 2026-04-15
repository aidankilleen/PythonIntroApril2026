

import numpy as np


data = np.random.randint(1, 100000, (5, 5))

print (data)

for row in data:

    for column in row:

        print (column, "\t", end="")

    print ()

print ("*" * 50)

print (f"{"Column1":^10}|{"Col 2":^15}|{"Col 3":^8}|{"Col 4":^20}")
for row in data:
    print (f"{row[0]:10}|{row[1]:<15}|{row[2]:^8}|{row[3]:20}")