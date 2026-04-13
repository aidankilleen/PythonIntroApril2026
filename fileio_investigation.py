# file_investigation.py

f = open("test.txt", "w")
lst = ["Alice", "Bob", "Carol", "Dan"]

for name in lst:
    f.write(f"{name}\n")

f.close()

f = open("test.txt", "r")

# print (len(f))

for item in f:
    print (item.strip())

# at this point we have reached the end of the file
# so f.readlines() returns nothing
lines = f.readlines()
print (lines)

f.close()

# python might close our file for us
# but it is good practice to close things ourselves

# we can use with to automatically close resources
with open("test.txt", "r") as f:
    for line in f:
        print (line.strip())

# f is automatically closed when we reach the end of the
# with block       








