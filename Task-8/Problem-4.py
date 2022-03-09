import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering','chennai' , 'campus'])
abc=ser.str.capitalize()
for i in abc:
    print(i,end=" ")