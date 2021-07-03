
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
    return render_template("index.html")

'''
@app.route('/login_signup')
def login():
    users = my_client.db.Quiz
    login_user = users.find_one({'email': request.form["username"]})

    if login_user:
        if bcrypt.hashpw(request.form["pass"].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return render_template("index.html")

    return 'Invalid username/password combination'
'''

@app.route('/courses/')

def courses():
    return render_template('courses.html')

if __name__ == '__main__':
    app.run(debug=True)
