import numpy as np

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])
print(np.vstack((arr1,arr2))) #vertical stack
print("\n", np.hstack((arr1,arr2))) #horizontal stack

#Spliting
arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(np.split(arr, 2)) #split into 2 equal parts