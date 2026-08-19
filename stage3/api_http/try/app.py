# create venv : python -m venv tryvenv
# activate it : source tryvenv/Scripts/activate
# install flask : python -m pip install flask
# create requirments.txt : python freeze > requirments.txt
# create api call : 

from flask import Flask, jsonify
app = Flask(__name__)
student = {
    "id":95,
    "name" : "Crazy",
    "branch":"CSE",
    "branch":"CSE",
    "age" : 20
}
@app.route("/student",methods=["GET"])
def get_student():
    return jsonify(student)
if __name__ == "__main__":
    app.run(debug=True)