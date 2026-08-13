# Create this Python data:
students = [
    {
        "name": "Mahantesh",
        "age": 20,
        "skills": ["Python", "SQL"]
    },
    {
        "name": "Rahul",
        "age": 21,
        "skills": ["Java", "C++"]
    }
]
#Convert it to JSON, then convert it back to Python and print each student's name and first skill.
import json
with open("question.json", "w") as file:
    json.dump(students,file,indent=4)

with open("question.json", "r") as file:
    print(json.load(file,))
    
for student in students:
    print(student["skills"[i]])