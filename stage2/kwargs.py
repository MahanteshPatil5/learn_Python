# similar concept to args for strings kwargs is used
# this is a dictionary type  data (arguments) is stored (passed) in key value pair  
# * tuples  ** dictionary

def func_kwargs(**kwargs):
    print("the function is kwargs")
    print("thi stores data in dictionary way")
    
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

student(name = "mahantesh", age= 20)
student(age=20, name="vinay",clas = 2)
student(name="vivek",sub="PCMB")

# when all three type of parameters are used it should be 
# def function(normal_paramter,*args,**kwargs):

# Easy
# Create a function that accepts any number of keyword arguments and prints the complete dictionary.
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

student(name = "mahantesh", age= 20)
student(age=20, name="vinay",clas = 2)
student(name="vivek",sub="PCMB")

# Create a function that prints only the "name" and "age" from **kwargs.
def name_age(**kwargs):
    for key,value in kwargs:
        if(key in ["name","age"]):
            print(key,value)
            
            
# or
def name_age(**kwargs):
    if "name" in kwargs:
        print(kwargs["name"])
    if "age" in kwargs:
        print(kwargs["age"])

# Create a function that loops through all keyword arguments and prints each key-value pair.
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
# Medium
# Create a function employee(**details) and print all employee details neatly.
def employee(**details):
    for key, value in details.items():
        print(key," ",value)
        
# Create a dictionary with your name, branch, and CGPA, then pass it to a function using ** unpacking.
employee = {
    "name":"vivek",
    "age" : 20,
    "branch" : "science"
}

def details(name,age,branch):
    print(name,age,branch)

details(**employee)

# Create a function that accepts **kwargs and checks whether the key "email" exists. If it exists, print it; otherwise print "Email not provided".
def employee(**details):
    if "email" in details:
        print(details["email"])
    else:
        print("email not provided")