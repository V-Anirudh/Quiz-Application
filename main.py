from flask import Flask, render_template, request, session, redirect
import pymongo
import jinja2
import bcrypt

app = Flask(__name__)
# MongoDb Connection

connection_String = "mongodb+srv://anirudh:anirudh55@cluster0.0qqke.mongodb.net/db_quiz?retryWrites=true&w=majority"
my_client = pymongo.MongoClient(connection_String)
db = my_client.db_quiz
Quiz = []


@app.route('/', methods=["GET", "POST"])

@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/login_signup/')
def login_signup():
    if request.method == "POST":
        name = request.form.get("fname")
        email = request.form.get("emailid")
        password = request.form.get("pwd")

        print(name, email, password)
        db.Quizs.insert_one({"name": name, "email": email, "password": password})
    return render_template("login_signup.html")


@app.route('/courses/')
def courses():
    return render_template('courses.html')


@app.route('/PythonQuiz/', methods=["GET", "POST"])
def python():
    return render_template('PythonQuiz.html')


@app.route('/JavaQuiz/')
def javaQuiz():
    return render_template('corejavaquiz.html')


@app.route('/JavaScriptQuiz/')
def javaScriptQuiz():
    return render_template('javascriptquiz.html')


@app.route('/DataStructuresQuiz/')
def DataStructuresQuiz():
    return render_template('datastructuresquiz.html')


@app.route('/CloudQuiz/')
def CloudQuiz():
    return render_template('cloudcomputingquiz.html')


if __name__ == '__main__':
    app.run(debug=True)
