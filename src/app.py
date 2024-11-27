from flask import redirect, render_template, request, flash, Response
#from flask_sqlalchemy import SQLAlchemy

from daos.reference_dao import ReferenceDao
from config import app, db
from db_helper import reset_db
from ref_enum import Reference

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
    datafields = ["type", "name","author","title","journal","year",\
                  "volume","number","pages","month","note",\
                    "howpublished","editor", "publisher"]
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
    references = reference_dao.get_references()
    bibtex_data = ""
    for ref in references:
        ref_data = f"@{ref[Reference.TYPE.value]}{ref[Reference.NAME.value]}\n"
        if ref[Reference.AUTHOR.value]:
            ref_data += f"  {ref[Reference.AUTHOR.value]}"
        bibtex_data += ref_data

    return bibtex_data

