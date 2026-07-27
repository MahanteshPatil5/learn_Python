# Dictionary 
# store data in key value pair 
# value can be accessed using key
student = {
    "name":"mahantesh",
    "age" :20
}

print(student["name"])

# use 
student.get("name")

# question
# Create a dictionary containing your name, age, and branch, then print only your branch.
me = {
    "name":"mahantesh",
    "age":20,
    "branch": "CSE"
}
print(me.get("branch"))

# Add a new key "CGPA" to the dictionary and print the complete dictionary.
me["CGPA"] = 8.6
print(me)
