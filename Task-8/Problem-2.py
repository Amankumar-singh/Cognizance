import numpy as np
#Taking input of number of element in array-1 and elements
number_element=int(input("length of array:-"))
list_1=[]
print("Enter  array_1 element:")
for i in range(number_element):
    print("enter element",i+1,":")
    first_element=int(input())
    list_1.append(first_element)
#Coverting array from  list1
array_1=np.array(list_1)

#Taking input of number of element in array-2 and elements
number_element2=int(input("length of array:-"))
#Throwing exception when user doesn't enter same no of element for Both array
if (number_element!=number_element2):
    raise TypeError("Both array element is not equal")
list_2=[]
print("Enter  array_2 element:")
for i in range(number_element2):
    print("enter element",i+1,":")
    second_element=int(input())
    list_2.append(second_element)
#Coverting array from  list1
array_2=np.array(list_2)

#verifing both array are equal or not  .
print(np.array_equal(array_1,array_2))