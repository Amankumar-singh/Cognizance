import numpy as np
#Taking input of number of element in array-1 and elements
number_element=int(input("length of array:-"))
list_1=[]
print("Enter elements for First Array:")
for i in range(number_element):
    first_element=int(input("Element :"))
    list_1.append(first_element)
#Coverting array from  list1
array_1=np.array(list_1)

#Taking input of number of element in array-2 and elements
number_element2=int(input("length of array:-"))
#Throwing exception when user doesn't enter same no of element for Both array
if (number_element!=number_element2):
    raise TypeError("Both array element is not equal")
list_2=[]
print("Enter elements for Second Array:")
for i in range(number_element2):
    second_element=int(input("Element :"))
    list_2.append(second_element)
#Coverting array from  list1
array_2=np.array(list_2)

#verifing both array are equal or not  .
print(np.array_equal(array_1,array_2))