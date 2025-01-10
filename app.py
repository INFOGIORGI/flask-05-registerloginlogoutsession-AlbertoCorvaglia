from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
