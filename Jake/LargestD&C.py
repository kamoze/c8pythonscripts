# Jake TUllY 2021-08-09
# Basic Divide and Conquer Algorithm to Find largest element without looping

import numpy as np
import math


# array of integer elements i = start index, j = end index

def largest(array, i: int, j: int):

    if (j-i) > 0:
        mid = math.floor((i+j)/2)
        left = largest(array, i, mid)
        right = largest(array, mid+1, j)
    else:
        return array[j]

    if left >= right:
        return left
    else:
        return right


a = np.array([3, 9, 12, 2, 22, 25, 78, 92, 77, 10, 35, 88, 45, 68, 15, 37, 15, 35, 45, 39, 87])
b = np.array([45, 12, 456, 2341, 85654, 8567, 6854, 564, 98, 56, 7, 56, 8, 65, 7, 6, 7, 56, 8, 54, 5, 7, 4])
c = np. array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])

x = largest(a, 0, a.size-1)
y = largest(b, 0, b.size-1)
z = largest(c, 0, c.size-1)

print(x)
print(y)
print(z)
