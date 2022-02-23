#problem :- Write a python program to make a 2-dimensional list that contains represents a table of records, for instance, student details like Roll no, Student Name, Marks; And complete the following 2 sub-tasks.
# i) Add some records in the list and print the list in tabular form,
row_1=['Roll no','Name','Marks']
list=[row_1]
no_record=int(input("How many record you want to enter:- "))   # here we are asking user for number of records he want to enter
for i in range(no_record):
    print('Fill the following details for ','Record no:-',i+1)
    row_2 = [input('Enter Roll no:- '),input('Enter Name:- '),input('Enter Marks:- ')] # taking input from user
    row_3 =row_2
    list.append(row_3)   #it will add the following items to existing list
print()
for i in list:  # here it will print  all data means table of records which we entered
    print(i[0]+'    '+i[1]+'    '+i[2])  

# ii) From created list, extract and print second record/row that contains 
if len(list)<3:   # here i am checking record 2 is present or not because acq i have to print record 2
    print("Record 2  not found ") 
else:               # it will print record 2
    print("RECORD 2")  
    print(list[2][0]+'  '+list[2][1]+'  '+list[2][2])