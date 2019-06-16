import numpy as np 

numbers = [1,2,3,4,5]

arr = np.array(numbers)

print(arr)

names = ['John', 'Tom', 'Jerry']

arr = np.array(names) 

print(arr) 

# 2 dimensional array
nested_list = [[1,2,3], [4,5,6]] 
arr = np.array(nested_list) 
print(arr)

# check dimensions of array
print(arr.ndim)

# check dtype 
print(arr.dtype)

arr = np.zeros(10)
print(arr)

arr = np.zeros((2,3))
print(arr)
