# mycopy.py

# using python mycopy.py source destination
# open the source file and copy the contents to the destination

# take 15 minutes to do this exercise
# 14:50

import sys


print ("mycopy")

args = sys.argv

print (args)

source = args[1]
dest = args[2]

fsource = open(source, "r")
fdest = open(dest, "w")

for line in fsource:
    fdest.write(line)

fsource.close()
fdest.close()

print (f"copied from {source} to {dest}")







