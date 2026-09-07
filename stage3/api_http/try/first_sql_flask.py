from flask import Flask,jsonify,request
import mysql.connector
app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Svce@2024",
    database = "LEARN_DB"
)
cursor = db.cursor()

@app.route("/")
def home():
    return "this is the home page"

@app.route("/students", methods= ["GET"])
def get_students():
    cursor.execute("select * from students")
    rows = cursor.fetchall()
    students = []
    for row in rows:
        students.append({
            "id" :row[0],
            "name":row[1],
            "branch":row[2]
        })
    return students
        
@app.route("/students", methods= ["POST"])
def post_students():
    
    data = request.get_json()
    
    if not data or "name" not in data or "branch" not in data:
        return "400 error bro enter proper data", 400
    
    cursor.execute("INSERT INTO students (name,branch) VALUES (%s,%s)",(data["name"],data["branch"]))
    db.commit()
    lastid = cursor.lastrowid
    return {"message" : "student created successfully ", "id" : lastid},201


@app.route("/students/<int:id>",methods=["PUT"])
def put_student(id):
    data = request.get_json()
    name = data["name"]
    branch = data["branch"]
    
    cursor.execute(
        "UPDATE students SET name=%s, branch=%s WHERE id= %s",(name,branch,id) 
    )
    db.commit()
    if cursor.rowcount == 0:
        return {"error":"student not found"},404
    
    return{
        "message":"student updated successfully"
    },200

@app.route("/students/<int:id>",methods=["PATCH"])
def patch_student(id):
    data = request.get_json()
    
    if "name" in data:
        cursor.execute(
            "UPDATE students SET name=%s WHERE id=%s",(data["name"],id)
        )
    
    if "branch" in data:
        cursor.execute(
            "UPDATE students SET branch=%s WHERE id=%s",(data["branch"],id)
        )
        
    db.commit()
    return{
        "message":"student partially updated"
    },200
    

@app.route("/students/<int:id>",methods=["DELETE"])
def delet_student(id):
    cursor.execute(
        "DELETE FROM students WHERE id =%s",(id,)
    )
    db.commit()
    if cursor.rowcount == 0:
        return {"error": "Student not found"}, 404
    return {
        "message":"student deleted successfully "
    },200
    
app.run(debug=True)
