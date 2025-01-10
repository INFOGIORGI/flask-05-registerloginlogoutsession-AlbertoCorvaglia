from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",title="HomePage")

@app.route("/register")
def register():
    return render_template("register.html",title="Register")

@app.route("/login")
def login():
    return render_template("login.html",title="Log In")

@app.route("/logout")
def logout():
    return render_template("logout.html",title="Log Out")

app.run(debug=True)