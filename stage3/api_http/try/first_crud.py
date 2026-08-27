# complete crud api with flask 

from flask import Flask,request
app = Flask(__name__)
students = [] # empty list

@app.route("/")
def home():
    return "u r in home page"

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

# read all
@app.route("/students", methods=["GET"])
def get_all_students():
    return students, 200

#read by id
@app.route("/students/<int:id>",methods= ["GET"])
def get_student(id):
    for student in students:
        if(student["id"] == id):
            return student,200
        
    return {"error" : " student not found"},404

#patch:
@app.route("/students/<int:id>", methods = ["PATCH"])
def patch_student(id):
    data = request.get_json()
    for student in students:
        if student["id"]==id:
            if "name" in data:
                student["name"] = data["name"]
            if "branch" in data:
                student["branch"]=data["branch"]
            return student,200    
    return {"messaages":"studen not fornd;"},404

# update put
@app.route("/students/<int:id>",methods=["PUT"])
def put_update(id):
    data = request.get_json()
    
    if not data or "name" not in data or "branch" not in data:
        return {"error": "PUT requires both 'name' and 'branch'"}, 400
    
    for student in students:
        if student["id"] == id:
            student["name"] = data["name"]
            student["branch"] = data["branch"]
        return student, 200
    return {"error":"student not found "},404

# delete
@app.route("/students/<int:id>",methods=["DELETE"])
def delete(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {"message ": "student deleted:: "},200
        
    return {"error ":"student not found"},404

app.run(debug=True)