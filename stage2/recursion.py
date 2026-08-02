# a function calls the same function itself untill a condition
# each time calling will smaller the problem cmp to previous
# 3 parts are there
# 1.base case
# 2.recursive case
# 3.progress towards basecase

# factorial of number
def factorial(num):
    if(num==1):
        return 1
    return num*factorial(num-1)
num = int(input("Enter a number to find its factorial : "))
fact = factorial(num)
print(fact)

# sum of first n number
def nsum(num):
    if(num==0):
        return 0
    return num+nsum(num-1)
sum = nsum(num)
print("Sum of first n numbers : ",sum)



# Easy
# Print numbers from 1 to n using recursion.
def numbers(n):
    if(n==0):
        return
    print(n)
    numbers(n-1)
    
    # or
    
    num=1  # wrong way
    if(num==n):
        return 
    print(num)
    numbers(num+1)
    
    
    # crt way
    if(num==0):return
    numbers(n-1)
    print(n)
    
# Print numbers from n to 1 using recursion.
def numbers(n):
    if(n==0):
        return
    print(n)
    numbers(n-1)
    
    
# Find the factorial of a number.
def factorial(num):
    if(num<=1):
        return 1
    return num*factorial(num-1)


# Find the sum of the first n natural numbers.
def sumn(num):
    
    if(num==0):
       return 0
    sum = num+sumn(num-1);
    
# Medium
# Find the sum of all elements in a list using recursion.
def sumlist(lst):
    if not lst:
        return 0
    return lst[0]+sumlist(lst[1:])
   
# Reverse a string using recursion.
def reverse(strin):
    if not string:
        return
    
# Check whether a string is a palindrome using recursion.
# Find the maximum element in a list using recursion.
# DSA Level (Try Later)
# Fibonacci using recursion.
# Binary Search using recursion.
# Generate all subsets of a list.
# Solve the N-Queens problem using recursion and backtracking.