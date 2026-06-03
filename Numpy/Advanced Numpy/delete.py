import numpy as np

arr = np.array([10,20,30,40,50])

print(np.delete(arr, 0)) #delete first element


arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("\n", np.delete(arr_2d, 0, axis=0)) #delete first row
print("\n", np.delete(arr_2d, 0, axis=1)) #