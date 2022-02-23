#problem:- Print the following pattern.
"""
    *
   * * 
  * * *
 * * * *
* * * * *

"""

# i have to print upper pattern and there is 5 row in that so we declearing a variable n and initialising with 5
n=5
row = 1
while row<=n:  # here i am using while loop for printing pattern.
    print(" "*(n-(row)),end="") 
    print("* "*(n-(n-row)))
    row=row+1