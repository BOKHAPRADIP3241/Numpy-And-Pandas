import numpy as np

arr = np.array([10,20,np.inf,40,-np.inf,60])

print(np.isinf(arr)) #check for inf values

cleaned_arr = np.nan_to_num(arr,posinf=999,neginf=-999) #replace inf with 999 and -inf with -999
print(cleaned_arr)
