from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Svce%402024@localhost/LEARN_DB"

db = SQLAlchemy(app)

# create your model
class Teacher(db.Model):
    __tablename__ = "teachers"
    
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable = False)
    subject = db.Column(db.String(20),nullable = False)
    
#add a teacher
with app.app_context(): 
    # create new table
    db.create_all()    
    # teacher = Teacher(
    # name = "Geeta",subject = "Home"
    # )
    # db.session.add(teacher)
    # db.session.commit()

# read datat in table

# teacher = Teacher.query.all()

@app.route("/")
def home():
    return "u r in home"

@app.route("/teacher",methods=["GET"])
def teachers_data():
    teachers = Teacher.query.all()

    if not teachers:
        return jsonify({"message": "no teachers found in databse"}),404
    
    teacher_list = []
    for teacher in teachers:
        teacher_list.append({
            "id": teacher.id,
            "name":teacher.name,
            "subject":teacher.subject
        })
    return jsonify(teacher_list),200


if __name__ == "__main__":
    app.run(debug=True)
    
