import pandas as aman

ser = aman.Series(['amrita', 'school', 'of', 'engineering','chennai' , 'campus'])
abc=ser.str.capitalize()
for i in abc:
    print(i,end=" ")