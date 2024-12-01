from flask import redirect, render_template, request
#from flask_sqlalchemy import SQLAlchemy

from daos.reference_dao import ReferenceDao
from config import app, db
from db_helper import reset_db


reference_dao = ReferenceDao(db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new_reference():
    return render_template("/new_reference.html")

@app.route("/references", methods=["GET"])
def references():
    refs = reference_dao.get_references()   # Fetch references from the repository
    view_as_bibtex = reference_dao.get_reference_view_format()
    return render_template("reference_list.html", references=refs, view_as_bibtex=view_as_bibtex)

@app.route("/change_list_format", methods=["POST"])
def set_bibtext_format():
    reference_dao.change_reference_view_format()
    return redirect("/references")

@app.route("/references", methods=["POST"])
def create_new_reference():  
    datafields = ["type", "name", "author", "title", "journal", "year", 
                  "volume", "number", "pages", "month", "note", 
                  "howpublished", "link", "editor", "publisher"]
    data = {}
    
    for field in datafields:
        field_data = None if request.form.get(field) == '' else request.form.get(field)
        data[field] = field_data

    reference_dao.create_reference(data)
    return redirect("/")


@app.route("/reset_db")
def reset_database():
    reset_db()
    return redirect("/")

@app.route("/export_bibtex")
def export_bibtex():
    bibtex_print = reference_dao.return_references_in_bibtex_form()

    return bibtex_print

@app.route("/edit_reference/<int:reference_id>")
def edit_reference(reference_id):
    reference = reference_dao.get_reference(reference_id)

    return render_template("edit_reference.html", reference=reference)

@app.route("/update_reference", methods=["POST"])
def update_reference():
    datafields = ["id", "type", "name","author","title","journal","year",\
                  "volume","number","pages","month","note",\
                    "howpublished","editor","link", "publisher"]
    data = {}
    for field in datafields:
        field_data = None if request.form.get(field) == '' else request.form.get(field)
        data[field] = field_data

    reference_dao.update_reference(data)
    return redirect("/references")

@app.route("/delete_reference/<int:reference_id>", methods=["POST"])
def delete_reference(reference_id):
    reference_dao.delete_reference(reference_id)
    return redirect("/references")

