from flask import Flask,request
app = Flask(__name__)
students = [] # empty list

#create::
@app.route("/students",methods=["POST"])
def create_student():
    data = request.get_json()
    student = {
        "id":len(students)+1,
        "name":data["name"],
        "branch":data["branch"]
    }
    students.append(student)
    return student,201

#read all
@app.route("/students/<int :id>",method= ["GET"])
def get_student(id):
    for student in students:
        if(student["id"] == id):
            return student,200
        
    return {"error" : " student not found"},404

#patch:
@app.route("/students/<int:id>", methods = ["patch"])
def update():
    data = request.get_json()
    for student in students:
        if(student["id"]==id):
            if "name" in data:
                student["name"] = data["name"]
            if "branch" in data:
                student["branch"]==data["branchs"]
            return students,200
        return {"messaages":"studen not fornd;"}