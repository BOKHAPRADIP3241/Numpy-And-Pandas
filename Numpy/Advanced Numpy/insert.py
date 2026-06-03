import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr)

new_arr = np.insert(arr,5,55,axis=None)
print(new_arr)

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)

new_arr_2d = np.insert(arr_2d,2,[10,20,25],axis=1)
print("\n",new_arr_2d)