# Problem : - Write a program to accept a string from the user and display characters, that are present at an even index number.

Input_String = input("Enter the String: ")  #here i am taking input from user
a = len(Input_String) #it will give length of input nuber
z=0   
for i in Input_String :  # here i am using for loop 
    if (z%2==0 & z<a): # here i am using if  statement and i given two contion if both condition satified then it will execute 
        print(Input_String[z])
    z=z+1  # each time when for loop run z value will increase by 1

    
