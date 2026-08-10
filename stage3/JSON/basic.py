# JSON = javascirpt object notation
# a text formate file which store the data and exchange the data 
# exchange data from and to  frontend and backend used JSON

# it supports data types like : string,boolean,number,object,array,null
# frontend send 
{
    "name" : "mahantesh",
    "age" : 20
}
# backend send
{
    "message" : "student registration sucessfully"
}

# in this way the data exchange is done in JSON

# JSON module : 
import json
# python to JSON  :: json.dumps()
# JSON to python    :: json.loads()

# example: 
student = {
    "name" : "mahantesh" ,
    "age"  : 20
}

data = json.dumps(student)
print(data)             # {"name" : "mahantesh", "age":20}

data2 = '{"name":"Mantu", "cgpa": 8.4}'
stud = json.loads(data2)
print(stud)             #{'name': 'Mantu', 'cgpa': 8.4}

# dumps(), dump(), loads(),load()

# dumps() ::  python object to json string 
# dump()  ::  python obkect to json file 
# loads() ::  json sting to python object
# load()  ::  json file to pyhton object

# JSON file example
# we have student.json (file)
# import json
student = {
    "name" : "Crazy",
    "age" : 22,
    "cgpa" : 8.4,
    "branch" : "CSE"
}

with open("student.json", "w") as file:
    json.dump(student,file)
    print("file created with name :  student.json")
with open("student.json", "r") as file:
    student = json.load(file)
print(student["name"],student["age"])


# always key in JSOn must be  strings

# questions
# Create a Python dictionary containing your name, age, branch, and skills. Convert it into a JSON string using dumps().
mydata = {
    "name" : "mahantesh", "age":20, "branch" : "CSE", "skills" : "FE,python,sql,C++"
}

# Take a JSON string and convert it back into a Python dictionary using loads().
with open("mydata.json","w") as myfile:
    json.dump(mydata,myfile)
with open("mydata.json","r") as myfile:
    mydata = json.load(myfile)
    
print("my data : ",mydata)
# Create student.json, store student information in it using dump(), then read it using load().