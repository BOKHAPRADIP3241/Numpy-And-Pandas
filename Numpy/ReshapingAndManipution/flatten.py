"""

ravel() --> It returns a flattened array. It does not create a copy of the original array, but instead returns a view of the original array whenever possible. This means that changes made to the flattened array will affect the original array.  
flatten() --> It also returns a flattened array. However, it always creates a copy of the original array, which means that changes made to the flattened array will not affect the original array.  

"""

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr.ravel())
print(arr.flatten())
