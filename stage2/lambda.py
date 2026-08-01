# a nameless function which is only for single work (task) 
# no name given to function only one time calculations will be done by that function
# lambda parameters : expression

lambda x:x*x  # return x*x (for x variable )

# use it like 
add = lambda a,b:a+b  # add = a+b (lambda is function)
print(add(10,20))

area = lambda l,b: l*b
print(area(10,3))

# no multiple statements are written there only a single expression will be written in this labda function
# used for consisness of a def function

# It is mainly used with built-in functions like:
# sorted()
# map()
# filter()
# reduce() (from functools)

# use with sorted()
students = [
    ("Ram", 80),
    ("Mahantesh", 95),
    ("Shyam", 75)
]

sorted(
    students,
    key = lambda student:student[1]       #based on the value it will differentiate (sort)
)

# use with map()
numbers = [1,2,3,4]
squre = list(map(lambda x:x*x ,numbers ))  # list of suare numbers  1,4,9,16

# use with filter()
even = list(filter(lambda x:x%2==0, numbers))  # finds the even of numbers




# Easy
# Create a lambda function to find the square of a number.
squre = lambda x:x*x

# Create a lambda function to add three numbers.
add3 = lambda a,b,c : a+b+c

# Create a lambda function to check whether a number is even or odd (return True or False).
even = lambda x:x%2==0

# Medium
# Given a list of numbers, use map() and a lambda to create a list of cubes.
nums = [1,2,3,4]
cubes = list(map(lambda x:x*x*x,nums))

# Given a list of numbers, use filter() and a lambda to keep only numbers greater than 10.
greater10 = list(filter(lambda x:x>10, nums))

# Given a list of tuples like:
students = [
    ("Ram", 80),
    ("Mahantesh", 95),
    ("Shyam", 75)
]
#Use sorted() with a lambda to sort the students by their marks.
sorted(
    students,
       key= lambda student: student[1])