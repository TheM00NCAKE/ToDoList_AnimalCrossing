import sqlite3
from datetime import datetime
class ToDoModel:
    con = sqlite3.connect('ToDoList.db')
    cur = con.cursor()
    try : 
        nb = cur.execute("SELECT COUNT(*) FROM ToDo").fetchone()[0] #récupère le nombre de tâches 
    except Exception :
        nb = 0
    con.close()
    def __init__(self,titre,libelle,date):
        self.titre=titre
        self.libelle=libelle
        self.date=date
    @staticmethod
    def get_nb():
        return ToDoModel.nb
    @staticmethod
    def add_task(titre, libelle):
        """Ajouter une tâche à la base de données."""
        con = sqlite3.connect('ToDoList.db')
        cur = con.cursor()
        cur.execute("INSERT INTO ToDo (Titre_task, Libelle_task, Date_tache_cree) VALUES (?, ?, ?)", 
                    (titre, libelle, datetime.now()))
        con.commit()
        con.close()
        ToDoModel.nb+=1
    @staticmethod
    def remove_task(index):
        con=sqlite3.connect('ToDoList.db')
        cur=con.cursor()
        cur.execute("""delete from ToDo where ID = ?""", (index,))
        con.commit()
        con.close()
        ToDoModel.nb-=1
    @staticmethod
    def get_tasks():
        con=sqlite3.connect('ToDoList.db')
        cur=con.cursor()
        cur.execute("""select * from ToDo""")
        taches=cur.fetchall() #prend tout les éléments pour les stocker dans taches
        con.close()
        return taches
    @staticmethod
    def update_task(index,t,l):
        con=sqlite3.connect('ToDoList.db')
        cur=con.cursor()
        cur.execute("""update ToDo set Titre_task=?, Libelle_task=? where ID=?""",(t,l,index))
        con.commit()
        con.close()
    @staticmethod
    def create_table():
        con=sqlite3.connect('ToDoList.db')
        cur=con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS ToDo (
                    ID INTEGER primary key AUTOINCREMENT,
                    Titre_task varchar(200),
                    Libelle_task varchar(300),
                    Date_tache_cree DATETIME)""")    #if not exists juste au cas où la base de données est déjà créé
        con.commit()
        con.close()