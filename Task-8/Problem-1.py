import numpy as np
print("Enter the first number")
first_number=int(input())
print("Enter the second number")
second_number=int(input())
#creating list with and between user input number
abc = list(range(first_number,second_number+1))
#convwerting into array
array1 = np.array(abc)
# user input vector
print("user input vector")
print(array1)
d = np.zeros([len(array1)+(len(array1-1)*(len(array1)-1))])
d[::len(array1)+1]=array1
#printing new vector
print("new vector")
print(d)