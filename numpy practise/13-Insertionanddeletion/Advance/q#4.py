# Delete a sub-array from a 2D numpy array at a specified index.


import numpy as np

arr = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

var = np.delete(arr,1,0)
print(arr)
print()
print(var)