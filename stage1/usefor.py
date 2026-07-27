name = "python"
for i in range(len(name)):
    print(name[i])

# or use

for ch in name:
    print(ch)  # use when no need of index
    
# next 
squre_of_num = []
for i in range(5):
    squre_of_num.append(i*i)

# use 
squre_of_num = [i*i for i in range(5)]


# while looping
password = ""
while password != "admin":
    password =input("Enter the password")
    
# use
# while condition:
    # work
    

# question

# Print numbers from 1 to 10.
for i in range(10):
    print(i)
    
    
# Print the multiplication table of 5.
for i in range(1,11):
    print(i*5);
# or 
table = [i*5 for i in range(10)]


# Print the sum of numbers from 1 to 10.
sum = [i+i for i  in sum(range(1,11))]
print(sum)


# Print each character of a String.
sting = "name"
for ch in sting:
    print(ch)




# while questions
# Print numbers from 10 to 1.
i = 10
while i>=1:
    print(i)
    
# Keep asking the user for a password until they enter "admin".
password =""
while password != "admin":
    password = input("enter correct password : ");