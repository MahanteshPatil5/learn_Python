from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABSE_URL"] = "mysql+mysqlconnector://DB_USER:DB_PASSWORD@DB_HOST/DB_NAME"

db = SQLAlchemy(app)

# create your model
class Teacher(db.Model):
    __tablename__ = "teachers"
    
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.string(20),nullable = False)
    subject = db.column(db.string(20),nullable = False)
    
#add a teacher
teacher = Teacher(
    nmae = "Geeta",subject = "Home"
)
db.session.add(teacher)
db.session.commit()

# read datat in table

teacher = Teacher.query.all()