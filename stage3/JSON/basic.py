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