# a funtion which need to be changed based on the arguments (paramters) 
# can be solved by this "args" concept 

# no need to change the function when arguments are chnaged 


# Suppose you write a function to add two numbers.
def add(a, b):
    return a + b

print(add(10, 20))

# Now tomorrow you want to add three numbers.
# print(add(10, 20, 30))
# Error!
# Now you change the function.
# def add(a, b, c):
    # return a + b + c

# if extra need then it should be again chnaged now think not to chnage  so use args

# ARGS
# this is a paramter in function which takes many values as tuples
# and work on that tuple

# function to find sum of n values using *args
def func_args(*args): # takes n value input(argument) 
    sum = 0
    for num in args:
        sum += num
    print(sum)

func_args(10,20,30,90,50)  #wokrs for many input no need of chnaging the duntions when no. of paramter chnges
 
 
# other example  unpaking using * 
values = [10,20,30] #list
def add(a,b,c):
    print(a+b+c)
add(*values)  #by using unpack (* unpack the list to numbers) and those are added
# unpack is [10,20,30] ti 10,20,30 (normal values)


# Coding Questions
# Easy
# Create a function that accepts any number of integers and prints them one by one.
# Create a function that accepts any number of integers and returns their sum.
# Create a function student(name, *marks) that prints the student's name and all marks.
# Medium
# Create a function that accepts any number of numbers and returns the largest number.
# Create a function that accepts any number of strings and prints only those whose length is greater than 5.
# Create a function that accepts any number of marks and returns the average.