import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])

print(arr[0:6])
print(arr[:6])
print(arr[1:6])
print(arr[::2])
print(arr[::-1])

#fancy indexing
print(arr[[1,2,6]])