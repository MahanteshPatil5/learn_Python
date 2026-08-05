# module is a simple python file which contain code which can be reused 
# it contains all function, variable , class , contraints
# make some files which have code of saparate things
# like database.py , auth.py , email.py this is called modularity (create saparate file then connect them so code ulook good)

# built in module  math , random , os , datatime , sys, json
# user defined (create a file then use it in other file so this is called)


# types 
# built in , use_definrd. created by develoopred

import math
print(math.sqrt(25))

# use
from math import sqrt #imported sqrt from math so no need of using mant.sqrt
print(sqrt(36))


#example  from math import factorial, sqrt 

# alising other concept
# use as  

import numpy as np # use as to short the word numpy to np
# use 
np.array()

#example import pandas as pd

# dir() function used to find what is inside module 

# 1. math module
# call  use from should,import math,naivile
math.factorial(9)
math.ceil(3.2) #upword value ceil value of the number
math.floor(3.2) #down word value  we can use some other too 
math.pi # built in pi value

# 2. random module 
# a module which is used for random values : generate ramdon things

# use 
import random #module random
random.randinit(1,10)  # this is used find the random value in the range 1 to 10
random.choice(list)   #used for finding a random choice of list 
random.shuffle(list) #this is used to shuffle the list randomly

# 3.Data time  used to find the date and time
# used in login page, attendence, file creation, backend api
from datetime import datetime
print(datetime.now())

# 4. json   
# module used for data exchange between frontend and backend 
# a dictionay 
student = {"name":"mahantesh", "age": 20}
import json
json.dumps(student) #dictionary to json 
json.loads(student) #json to dictionary

