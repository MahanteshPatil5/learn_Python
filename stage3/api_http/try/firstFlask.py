from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "hello world"


@app.route("/about")    #use /about to run this function
def about():
    return"HEllo bro i am in about section"
app.run()