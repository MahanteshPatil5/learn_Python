# Coding Questions
# Easy
# Import the math module and print the square root of 64.
print("Hello")
from math import sqrt
print("squre root of 64 : ",sqrt(64))

# Generate a random number between 1 and 100 using random.
import random
print("randomly generated number : ",random.randint(1,100))
# Print the current date and time using datetime.
from datetime import datetime
print("current time and date ",datetime.now())
# Print the current working directory using os.
import os
print("current working directory : ",os.getcwd)
# Medium
# Create your own module calculator.py with functions add(), sub(), mul(), and div(). Import it into main.py and use all four functions.
import cal
print("sum oof 10,20 : ",cal.add(10,20))
print("substraction of 70,1 : ",cal.sub(70,1))
print("multiflication of 12, 14: ",cal.mul(12,14))
print("division of 20,2: ",cal.div(20,2))

# Create a Python dictionary representing a student, convert it to JSON using json.dumps(), then convert it back using json.loads().
