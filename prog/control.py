from flask import Flask, render_template, request, redirect, url_for
from model import ToDoModel
from pathlib import Path
#faire en sorte que les éléments comme la feuille de style et les images sont récupérés correctement
path = str((Path(__file__).parent).parent / 'templates') 
path2 = str((Path(__file__).parent).parent / 'static')
app = Flask(__name__, template_folder=path, static_folder=path2)

@app.route("/")
def index():
    ToDoModel.create_table()
    tasks=ToDoModel.get_tasks()   #va afficher toutes les tâches dès l'ouverture de la page
    return render_template("index.html", tasks=tasks,nb=ToDoModel.nb)
@app.route("/add_task", methods=["POST"])
def add_task():
    titre = request.form.get("task")
    libelle = request.form.get("libelle")
    if titre:  
        ToDoModel.add_task(titre, libelle)
    return redirect(url_for("index"))
@app.route("/remove/<int:index>",methods=['GET', 'POST'])
def remove_task(index):
    ToDoModel.remove_task(index)
    return redirect(url_for("index"))
@app.route("/update/<int:index>", methods=['GET','POST'])
def update_task(index):
    t=request.form.get("t")
    l=request.form.get("l")
    ToDoModel.update_task(index,t,l)
    return redirect(url_for("index"))