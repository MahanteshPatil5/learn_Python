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



# next concept 
# Default value in functions
# in function parameter use = so i default parameter
# def function_name(parameter=default_value):
    # code
# exmple
def greet(name="guest"):
    print(f"hello {name}")

# where they are used 
def connect(host = "localhost"):
    #code
    print("using localhost")
def createrole(role="student"):  #if not parameter given then this default will be used 
    #code
    print("used createrole function")
    
    
# next concept 
# Keyword Argument
# give keyword and arguement name (so that remembering key and value will be easy)

def student(name,age):
    print(name,age)
    
student("mahatesh",20)
student(name = "vivek", age=18)  #good way of writing
student(age=18,name = "vinay")  # this is also allowed #good way of writing


# where it is used
def createuser(name,age,id):
    print(f"created user {name} {id}")
createuser(name="mahantesh",age=20,id="24cs99")


# Create a function welcome() that prints "Welcome" by default, but allows a custom name if provided.
def welcome(name=None):
    print(f"Welcome!.. {name}")

# Create a function calculate_price(price, tax=18) that prints the total price after adding tax.
def calculate_price(price,tax=18):
    price = price+(price*(tax/100))
    print(f"total price : {price}")
    
# Create a function student(name, branch="CSE", year=2) and call it in three different ways.
def student(name,branch="cse",year=2):
    print(f"hello {name} ur from {branch} in {year} year")
    
student("mahatesh")
student(branch="ISE",year=3,name="vivek")  #good way of writing
student("vinay",branch="AI" , year=1) 

# Create a function employee(name, age, salary) and call it using keyword arguments in a different order.


# Create a function book(title, author="Unknown") and test it with and without the author argument.