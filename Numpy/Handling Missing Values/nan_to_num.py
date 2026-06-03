import numpy as np

arr = np.array([10,20,np.nan,40,np.nan])

cleaned_arr = np.nan_to_num(arr,nan=20) #replace nan with 0
print(cleaned_arr)

