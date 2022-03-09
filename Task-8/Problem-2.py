import numpy as np
n=int(input("Enter array length:"))
ar1=[]
ar2=[]
print("Enter elements for First Array:")
for i in range(n):
    e=int(input("Element :"))
    ar1.append(e)
print()    
print("Enter elements for Second Array:")   
for j in range(n):
    e1=int(input("Element :"))
    ar2.append(e1)
    
ar1=np.array(ar1)
ar2=np.array(ar2)
print()
print("First array: ",ar1)
print("Second arrary: ",ar2)
print()
c=ar1==ar2
eq=c.all()
print(eq)  