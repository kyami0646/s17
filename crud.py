from flask import  Blueprint,redirect, render_template, request,redirect,g
from flask_login import login_required,current_user
from .models import Textbook
from . import db

crud = Blueprint('crud',__name__)

id = 1

@crud.route("/textbook_register" ,methods=["GET","POST"])
@login_required
def textbook_register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    all_page = request.form.get("all_page")
    if not all_page:
        return render_template("failure.html")

    new_textbooks=Textbook(name=name,all_page=all_page,user_id=current_user.id)
    db.session.add(new_textbooks)
    db.session.commit()
    return redirect("/textbooks")

@crud.route("/textbooks" ,methods=["GET","POST"])
@login_required
def textbooks():
    textbooks = Textbook.query.all()
    return render_template("textbook_register.html", textbooks=textbooks)

@crud.route("/updata" ,methods=["GET","POST"])
@login_required
def updata():
    global id 
    id = request.form.get("id")
    text_id = Textbook.query.filter_by(id=id).all()
    return render_template("edit.html",text_id = text_id)


@crud.route("/edit" ,methods=["GET","POST"])
@login_required
def edit():
    current = request.form.get("current_page")
    update = db.session.query(Textbook).filter_by(id=id).first()
    update.current_page=int(current)
    db.session.add(update)
    db.session.commit()
    all = Textbook.query.filter_by(id=id).first().all_page
    per = int(current)/all
    status = Textbook.query.all()
    return render_template("status.html",status=status,per=per)

@crud.route("/time" ,methods=["GET","POST"])
@login_required
def time():   
    time = request.form.get("time")
    update = db.session.query(Textbook).filter_by(id=id).first()
    update.accumulated_time += int(time)
    db.session.add(update)
    db.session.commit()
    current=Textbook.query.filter_by(id=id).first()
    TIME=current.accumulated_time
    status = Textbook.query.all()
    return render_template("status.html",status=status,TIME=TIME)


@crud.route("/delete" ,methods=["GET","POST"])
@login_required
def delete():   
    delete=db.session.query(Textbook).filter_by(id=id).first()
    db.session.delete(delete)
    db.session.commit()
    status = Textbook.qery.all()
    return render_template("status.html",status=status)
    