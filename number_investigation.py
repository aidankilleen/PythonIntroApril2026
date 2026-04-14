# number_investigation.py

n = 10

print (n)

# python can natively handle binary numbers
n = 0b10000
print (n)
print (f"{n:b}")

# hex
n = 0xff
print (n)
print (f"{n:x}")

# oct
n = 0o77
print (n)
print (f"{n:o}")

n = 0b1000000

print (f"{n:b}")

while n > 0:
    print (f"{n:08b}")
    n >>= 1


name = "aidan"
city = "Cork"
phone = "087 1234567"

print (f"{'Name':^10}|{'City':^20}|{'Phone':^13}")
print ("-" * 50)
print (f"{name:>10}|{city:20}|{phone:13}")




