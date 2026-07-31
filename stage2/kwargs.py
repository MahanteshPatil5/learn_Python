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

    