# a file that stores the data parmentaly is called file 
# like student.txt, photos.jpeg

# a file is created when u open a file
# if a file exist then all operation done on that file only if it is not existing then new one is created

file = open("student.txt" , "r")
print(file.read(15))

creat = open("createdfile.txt", "a") # a new file is created and in append mode
print(creat.write("Hi broo this is file created in append mode")) # write to file
print(creat.write("\n this is just appended to the existing file")) #just added new line

file.close()
creat.close()  #closed both the filess