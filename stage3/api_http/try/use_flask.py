from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"



student = {
    "id":95,
    "name" : "Crazy name in useflask",
    "branch":"CSE",
    "core":"cse",
    "age" : 20
}
@app.route("/student", methods= ["POST","GET"])
def create_student():
    if request.method=="GET":
        return jsonify(student)
    if request.method=="POST":
        newdata = request.get_json(force=True)
        if newdata:
            student.update(newdata)
        return jsonify({"message":"student created "})
if __name__ == "__main__":
    app.run (debug=True)


# the flask which create api and used in tryflask.py 
# function shows some data if it wants to get data data can be taken from tryflask.py