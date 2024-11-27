from flask import redirect, render_template, request #jsonify, flash
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
    try:
        references = reference_dao.get_references()

        bibtex_data = ""
        for ref in references:
            ref_type = ref.get("type", "misc")
            if ref_type == "article":
                bibtex_entry = f"""
                @article{{{ref["year"]}{ref["name"]},
                  author = {{{ref["author"]}}},
                  title = {{{ref["title"]}}},
                  journal = {{{ref["journal"]}}},
                  year = {{{ref["year"]}}},
                  volume = {{{ref["volume"]}}},
                  number = {{{ref["number"]}}},
                  pages = {{{ref["pages"]}}},
                  month = {{{ref["month"]}}},
                  note = {{{ref["note"]}}}
                }}
                """
            elif ref_type == "book":
                bibtex_entry = f"""
                @book{{{ref["year"]}{ref["name"]},
                  author = {{{ref["author"]}}},
                  editor = {{{ref["editor"]}}},
                  title = {{{ref["title"]}}},
                  publisher = {{{ref["publisher"]}}},
                  year = {{{ref["year"]}}},
                  volume = {{{ref["volume"]}}},
                  number = {{{ref["number"]}}},
                  pages = {{{ref["pages"]}}},
                  month = {{{ref["month"]}}},
                  note = {{{ref["note"]}}}
                }}
                """
            else:
                bibtex_entry = f"""
                @misc{{{ref["year"]}{ref["name"]},
                  author = {{{ref["author"]}}},
                  title = {{{ref["title"]}}},
                  howpublished = {{{ref["howpublished"]}}},
                  year = {{{ref["year"]}}},
                  month = {{{ref["month"]}}},
                  note = {{{ref["note"]}}}
                }}
                """
            bibtex_data += bibtex_entry

        return Response(
            bibtex_data,
            mimetype="text/plain",
            headers={"Content-Disposition": "attachment;filename=references.bib",
		"Content-Type": "application/x-bibtex"
	    }
        )
    except Exception as e:
        flash(f"Virhe BibTeX-tiedoston luomisessa: {str(e)}", "error")
        return redirect("/")
