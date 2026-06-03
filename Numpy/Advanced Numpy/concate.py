"""
np.concatenate((array1, array2), axis=0)

axis=0 : vertical concatenation
axis=1 : horizontal concatenation
"""

import numpy as np

arr1 = np.array([10,20,30,40,50])
arr2 = np.array([60,70,80,90,100])

print(np.concatenate((arr1,arr2), axis=0))
# print(np.concatenate((arr1,arr2), axis=1)) #error

arr_2d_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2d_2 = np.array([[10,20,30],[40,50,60],[70,80,90]])

print("\n",np.concatenate((arr_2d_1,arr_2d_2), axis=0))
print("\n",np.concatenate((arr_2d_1,arr_2d_2), axis=1))