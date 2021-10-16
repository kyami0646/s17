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
    return render_template("home.html", number = number)    


@app.route("/textbook_register" ,methods=["GET","POST"])
def textbook_register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    all_page = request.form.get("all_page")
    if not all_page:
        return render_template("failure.html")

    engine.execute('INSERT INTO textbooks(name,all_page,user_id) values(?,?,?)',name,all_page,1)
    return redirect("/textbooks")

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


@app.route("/textbook_Delete" ,methods=["GET","POST"])
def edit():
    current = request.form.get("current_page")
    engine.execute('UPDATE textbooks SET current_page = ? where id = ?',current,id)
    status = engine.execute('SELECT *FROM textbooks')
    return render_template("status.html",status=status)

@app.route("/delete" ,methods=["GET","POST"])
def delete():   
    engine.execute('DELETE from textbooks WHERE id = ?',id)
    status = engine.execute('SELECT *FROM textbooks')
    return render_template("status.html",status=status)
    
if __name__ == "__main__":
    app.run()