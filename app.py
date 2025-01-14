from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "138.41.20.102"
app.config["MYSQL_PORT"] = 53306
app.config["MYSQL_USER"] = "ospite"
app.config["MYSQL_PASSWORD"] = "ospite"
app.config["MYSQL_DB"] = "w3schools"

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html",title="HomePage")

@app.route("/register/",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html",title="Register")
    else:
        cursor = mysql.connection.cursor()              
        username = request.form.get("username")
        cognome = request.form.get("cognome")
        nome = request.form.get("nome")
        pwd = request.form.get("password")
        pwd_confirm = request.form.get("confirmPassword")
        
        if username == "" or cognome == "" or nome == "" or pwd == "" or pwd_confirm == "":
            return render_template("/register.html", message="Compila tutti i campi <3")
        else:
            if pwd == pwd_confirm:
                #controllo se esiste utente        
                query = "SELECT username FROM users WHERE username=%s"
                cursor.execute(query,(username,))
                db_users = cursor.fetchall()
                if len(db_users)>0:
                    if username in db_users[0]:
                        return render_template("/register.html", message="Nome utente già esistente")
                else:
                    query = "INSERT INTO users VALUES(%s,%s,%s,%s)"
                    cursor.execute(query,(username,pwd,nome,cognome))
                    mysql.connection.commit()        
                return redirect("/")
            else:
                return render_template("/register.html", message="Password non corrispondenti")


@app.route("/login/")
def login():
    return render_template("login.html",title="Log In")

@app.route("/logout/")
def logout():
    return render_template("logout.html",title="Log Out")

app.run(debug=True)