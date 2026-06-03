

#Boolean masking

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[arr > 2])
print(arr[(arr > 5) & (arr < 9) | (arr == 1)])