import numpy as np

arr1=np.array([0,1,2,3,4,5])
arr2=np.array([5,6,7,8,9,0])
print("array1:",arr1)
print("array2:",arr2)
print("Common elements:",np.intersect1d(arr1,arr2))