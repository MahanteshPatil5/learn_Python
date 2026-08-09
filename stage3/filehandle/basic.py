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


# there are three operation in file handeling 
# like READ WRITE APPEND 
# when file opened in read op then we only reading the file content,  without chnaging the content
# file opened in write mode , file is allowed read and write  ,  when writing all the existing data is earased no content is remaining  
# file opened in append mode is allowed to read write  and no existing data us removed we can write some new but written at last 

# when a file is opened then python will create some file objects keeps track of : 
# which file is opened 
# current reading position (cursur)
# opening mode(read/write)

# Cursur
# this will keep tracking of which word of content of file is reading/writing
# act like a point keep track of letter in word

# file has Hello world
file.read(5) # hello (printed) 
# cursur is at " " space 
# python will read after the space if called again

# tell() (function used to know where the cursor is pointing to)
file.tell() # tell the index where cursur is pointing to


# seek() function used to bring back the cursur
file.seek(0) #cursur back to 0


# with  is used
# when a file is opened and doing some action on it and got an error before close so that file will never close 
# so to close if an error occures also with is used
with (open("student.txt","a"))as file:
    print(file.read())    #after complting block automaticaly file is closed
    
# some methods 
# read() to read all content of a file
# readline() to one line of file
# readlines() to read all content line by line 

