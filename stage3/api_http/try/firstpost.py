from flask import Flask,jsonify,request
app = Flask(__name__)
students = []

@app.route("/")
def home():
    return "this is home page"


@app.route("/students",methods=["POST"])
def create_students():
    data = request.get_json()
    if not data or "name" not in data or "branch" not in data:
        return {"error":"name and branch are requested"},400
    student = {
        "id": len(students)+1,
        "name": data["name"],
        "branch":data["branch"]
    }
    students.append(student)
    return student,201
if __name__ == "__main__":
    app.run(debug=True)
    
    