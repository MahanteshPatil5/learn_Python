age = input("Enter age : ")

if(age>18):
    print("U r major u can vote")
else:
    print("minor nt eleigble for voting");

# ()
marks = input("Enter ur marks : ")
attendence = input("Entter the marks : ")

# instead
# if marks >= 35:
#     if attendance >= 75:
#         print("Pass")
# use 
if marks>35 and attendence>85:
    print("U r eligble for vote")

# style 2
# instead of

# if fruit == "Apple" or fruit == "Mango" or fruit == "Orange":
#     print("use below way");
# # use 
# if fruit in ["apple",'banana',"orange"]:

# Question 
# Check whether a number is positive or negative.
num = float(input("enter a number : "))
print("number negative") if num<0 else print("number is positive")


# Check whether a number is even or odd.''
print("even ") if num%2==0 else print("odd")

# Find the larger of two numbers.
n1 ,n2 = 10,5
large = n1 if n1>n2 else n2

# Check whether a person is eligible to vote (18+).
age = input("Enter the age : ")
print("older eligble") if age>=18 else print(" not eligible") 