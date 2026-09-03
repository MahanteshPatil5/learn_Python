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
    
    data = request.get_json({
    "name": "Vivek",
    "branch": "MBBS"
})
    
    if not data or "name" not in data or "branch" not in data:
        return "400 error bro enter proper data", 400
    cursor.execute("INSERT INTO STUDENTS VALUES (%s,%s)",("name", "branch"))
    db.commit()
    last = cursor.lastrowid()
    return {"message" : "student created successfully ","id" = last}

app.run(debug=True)
