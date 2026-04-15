# numpy_investigation.py

import numpy as np


arr = np.array([1,2,3])

print (arr)

arr = np.random.randint(1, 10, (4, 4))

print (arr)

l1 = [1, 2, 3]
l2 = [6, 5, 4]

# generally in python the operators work if they make sense
print (l1 + l2)
print (l1 * 3)

# this works in numpy
mx1 = np.random.randint(1, 10, (4, 4))
mx2 = np.random.randint(1, 10, (4, 4))

print (mx1)
print (mx2)

print (mx1 + mx2)

print (mx1 * 5)

print (mx1 * mx2)


arr = np.array(range(1, 17))

print (arr)

arr = arr.reshape((4, 4))
print (arr)

# numpy has extra slicing operations

# slice rows
print (arr[1:3])

# slice columns
print (arr[:,1:3])

# slice section
print (arr[1:3,1:3])

arr = np.zeros((4, 4))
print (arr)

arr = np.ones((4, 4))
print (arr)














