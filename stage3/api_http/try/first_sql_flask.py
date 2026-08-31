from flask import Flask,jsonify
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
        

app.run(debug=True)
