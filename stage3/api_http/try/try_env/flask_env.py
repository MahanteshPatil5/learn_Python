from flask import Flask,request
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")   
)
cursor = db.cursor(dictionary=True)

@app.route("/")
def home():
    return "hhi bro u r in home of getenv file"

@app.route("/students",methods=["GET"])
def student_data():
    cursor.execute("select * from students")
    students = cursor.fetchall()
    # students = []
    # for row in rows:
    #     students.append({
    #         "id":row[0],"name":row[1],"branch":row[2]
    #     })
    return students,200

app.run(debug=True)