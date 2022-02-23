# Problem :- Write a program to check if the given number is a palindrome number. 

def p_n(num):
    if len(num) == 1 : # if input number's length is 1 then it's always palindrome that's why i am using if statement here which give true when length of input number is 1
        return True
    if num[0] == num[len(num) - 1] :
        return p_n(num[1:len(num) - 1]) # i am using recursion here basicaly it will call itself 
    else:
        return False
number = input("Enter any number for checking , Number is palindrome number or not:-") # i am taking input number from user

#now if method return true then if statement in line 13 will execute and if it's return false then else statement in lie 15 will execute 
if(p_n(number)): 
    print("Input number is a Palindrome number")
else:
    print("Input number is not a Palindrome number")

