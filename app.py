from os import name
from flask import Flask, redirect, render_template, request,redirect,g
from sqlalchemy import create_engine


app = Flask(__name__)

engine = create_engine('sqlite:///textbook.db')
id = 1


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")    


@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("register.html")
    

@app.route("/home", methods={"GET","POST"})
def home():
    number = 50
    number2 = 30
    return render_template("home.html", number = number, number2 = number2)    


@app.route("/textbook_register" ,methods=["GET","POST"])
def textbook_register():
    
    return render_template("textbook_register.html")

@app.route("/textbooks" ,methods=["GET","POST"])
def textbooks():
    textbooks = engine.execute('SELECT * FROM textbooks')
    return render_template("textbook_register.html", textbooks=textbooks)

@app.route("/updata" ,methods=["GET","POST"])
def updata():
    global id 
    id = request.form.get("id")
    text_id = engine.execute('SELECT * FROM textbooks WHERE id=?',id)
    return render_template("edit.html",text_id = text_id)

@app.route("/record" ,methods=["GET","POST"])
def record():
    return render_template("record.html")

@app.route("/textbook_Delete" ,methods=["GET","POST"])
def edit():
    return render_template("textbook_Delete.html")
@app.route("/delete" ,methods=["GET","POST"])
def delete():   
    engine.execute('DELETE from textbooks WHERE id = ?',id)
    status = engine.execute('SELECT *FROM textbooks')
    return render_template("status.html",status=status)
    
if __name__ == "__main__":
    app.run()