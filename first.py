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
arr1 = np.arange(0,9)    #numpy method(arange -> start from 0 and end with 8 i.e last number is not consider)
arr2 = np.arange(0,11,2)  #arange all even number between 0 to 11 
print(arr1)
print(arr2)

arr3 = np.zeros(1)   # numpy method zeros-> print in output one zero
arr4 = np.zeros(4)   #print in output 4 zero
arr5 = np.zeros((3,5))   # print in output 3 rows and 5 column zeros
print(arr3)
print(arr4)
print(arr5)


arr6 = np.ones(3)   # numpy ones method print in output 4 ones
arr7 = np.ones((4,5))  #print in output 4 row and 5 column ones
print(arr6)
print(arr7)

arr8 = np.linspace(0,5,10)  #  numpy linspace start with 0 and end with 5 and getting 10 evenly point in between 0 to 5
print(arr8)     

arr9 = np.eye(4)  # numpy eye method  print 2-d array with identity matrices
print(arr9)

import numpy as np       # create an array using numpy arange method
arrr = np.arange(0,11)    # start with 0 and end with 10
print(arrr)

arrrr = np.array([0,1, 2, 3, 4,5,6,7,8,9,10])
print(arrrr[1:5])    # array indexing with slice method


