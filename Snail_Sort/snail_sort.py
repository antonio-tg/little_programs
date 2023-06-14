# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(array)
print(snail(array))
