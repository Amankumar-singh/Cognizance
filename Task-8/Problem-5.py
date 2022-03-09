import string
import numpy as np
#1 Addition of two numpy arrays
print("<---------------1 . Addition of two numpy Azrray-------------->")
#Creating two arrays '"arr1" and "arr2"
array_1=np.array([25,24,33,65,42])
array_2=np.array([26,32,28,25,45])

#Adding both the arrays and printing the sum
print(array_1+array_2)

#4 Array Datatype Conversion
print("<---------------4 . Array Datatype Conversion-------------->")
array_1 = np.array([ 55.5, 45.5, 21.3 ,14.6,99.9])
print(array_1.astype(int))