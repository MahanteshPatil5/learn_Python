# Easy
# Create a file student.txt and write your name and branch into it.
file = open("student.txt","a")
file.close()

# Read the entire contents of student.txt.
file = open("student.txt","r")
print(file.read())

# Read only the first line of a file.
print(file.readline())

# Append your CGPA to the same file.
with open("student.txt","a") as file:
    file.write("cgpa :8.2")
with open("student.txt","r") as file:
    print(file.read())


# Medium
# Count the number of lines in a text file.
count = 0
with open("student.txt","r") as file:
    for line in file:
        count = count+1
print("lines in file is : ",count)   
 
# Count the number of words in a text file.

word_count=0
with open("student.txt","a") as file:
    for line in file:
        words = line.split()
        word_count += len(words)
print("Total words : ",word_count)

# Copy the contents of one file into another.
with open("student.txt","r") as srcfile:
    content = srcfile.read()
with open("student.txt","w") as desfile:
    desfile  = desfile.write(content)


# Read a file line by line and print line numbers like:
with open("student.txt","r") as file:
    for linenum,line in enumerate(file,start=1):
        print(f"{linenum}.{line}")
        