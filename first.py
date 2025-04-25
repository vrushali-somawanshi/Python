# import numpy as np
 
# # Create a Numpy array
# array = np.array([1, 2, 3, 4, 5])
 
# # Perform basic operations
# print("Original array:", array)
# print("Array multiplied by 2:", array * 2)
# print("Array squared:", array ** 2)
 
# # Calculate the mean and standard deviation
# mean = np.mean(array)
# std_dev = np.std(array)
 
# print("Mean of the array:", mean)
# print("Standard deviation of the array:", std_dev)

import numpy as np     # numpy library np is object
array = np.array([1,2,3,4,5]) # create np array
print(array)
 
list = [[1,2,3],[4,5,6],[7,8,9]]  # create 2-d array (two square bracket start and end with 3 rows and 3 columns)
arr = np.array(list)
print(arr)

#numpy methods
arr = np.arange(0,9)    #numpy method(arange -> start from 0 and end with 8 i.e last number is not consider)
arr = np.arange(0,11,2)  #arange all even number between 0 to 11 

arr = np.zeros(1)   # numpy methodzeros-> print in output one zero
arr = np.zeros(4)   #print in output 4 zero
arr = np.zeros((3,5))   # print in output 3 rows and 5 column zeros

print(arr)



