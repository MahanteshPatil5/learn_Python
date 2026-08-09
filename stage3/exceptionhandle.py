# when an error ocurs during runing a problem the whole probelm crashes
# to stop that to happen python handel that errby using Exception handel concept

# to handle an exception python uses try, except clause
try:
    age = int(input("Enter ur age : "))
except ValueError:
    print("Enter a number :: ") # if value 20 normal flow ,if it is string then an err and print the except err

# some type of exception errors:
# 1.ValueError. 2.TypeError 3.IndexError 4.ZeroDividionError
# 5.KeyError 6.FileNotFoundError 

# multiple catching
try:
    age= int(input("Enter ur age : "))
    a=int(input("Enter a value : "))
    b=int(input("Enter b avalue ; "))
    print(a/b)
except ValueError:
    print('Enter the age avlue a number: ')
except ZeroDivisionError:
    print("Enter the b value > 0 ")
    
    
# else  :: runs when no exception occurs: 
else:    #when no error
    print("You entered : ",age)
    
# finaly :: runs whenever an exceptiion occur or not
finally:  #this runns after all except and try done
    print("finished")



# getting errors
try:
    result = 10/0
except ZeroDivisionError as error:
    print(error)              # output : ZeroDividsionError
    

# raise
age = int(input("Enter ur age : "))
if age<18:
    raise ValueError("Age should be abouve 18 ")

