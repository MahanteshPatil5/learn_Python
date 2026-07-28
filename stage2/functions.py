# functions 
# blcok of code that perform a specific task when called
# area of rectangle

def area(length,breadth):
    return length*breadth

# define
def great():
    print("Hello GN")
# call
great()

# Parameter → variable in the function definition.
# Argument → actual value passed when calling the function.

# Questions

# Create a function that prints "Welcome to Python".
def welcome():
    print("Welcome to python")
# Create a function that takes your name as a parameter and prints a greeting.
def greet(name):
    print("Hello bro ",name)
    
# Create a function that takes two numbers and returns their sum.
def sumlofnumber(a, b):
    return a+b

# Create a function that returns the square of a number.
def squre(n):
    return n*n

# Create a function that returns both the quotient and remainder of two numbers.
def QandR(a,b):
    quetient = a/b
    remender = a%b
    return quetient,remender

# Create a function that checks whether a number is even or odd and returns the result.
def check(a):
    if (a%2==1):
        return "even"
    else:
        return "odd"
