from flask import redirect, render_template, request
import requests
from entities import acm_scraper

from daos.reference_dao import ReferenceDao
from config import app, db
from db_helper import reset_db
import re

reference_dao = ReferenceDao(db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new_reference():

    return render_template("/new_reference.html", errors=None)

@app.route("/references", methods=["GET"])
def references():
    refs = reference_dao.get_references()
    view_as_bibtex = reference_dao.get_reference_view_format()

    return render_template("reference_list.html", references=refs, view_as_bibtex=view_as_bibtex, selected_references=[])

@app.route("/change_list_format", methods=["POST"])
def set_bibtext_format():
    reference_dao.change_reference_view_format()
    return redirect("/references")

@app.route("/references", methods=["POST"])
def create_new_reference():
    errors = []

    datafields = ["type", "name", "author", "title", "journal", "year", 
                  "volume", "number", "pages", "month", "note", 
                  "howpublished", "link", "editor", "publisher"]
    data = {}
    
    if request.form.get("type") == "acm":
        link = request.form.get("link")
        html = requests.get(link).content
        data["link"] = link
        
        if "book" in link:
            data = acm_scraper.scrape_book(html)
        else:
            data = acm_scraper.scrape_article(html)
    for field in datafields:
        if field in data:
            continue
        
        field_data = None if request.form.get(field) == '' else request.form.get(field)
        data[field] = field_data

    all_names = reference_dao.get_all_names()
    reference_name = request.form["name"].lower()

    if reference_name in all_names:
        errors.append("Keyword already in use!")

    valid_name_format = re.compile(r"^[a-zA-Z0-9]+$")
    if not re.fullmatch(valid_name_format, reference_name):
        errors.append("Keyword should contain only numbers and/or letters and no spaces.")

    if request.form.get("pages"):
        reference_pages = request.form["pages"]

        if reference_pages != None:
            valid_pages_format = re.compile(r"(\d{1,4}(-[1-9]\d{0,3})?)?")
            if not re.fullmatch(valid_pages_format, reference_pages):
                errors.append("Pages needs to be written as a number or two numbers divided by a dash (e.g. 1 or 1-25)")
 
        
    if errors:
        return render_template("/new_reference.html", errors=errors)

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

@app.route("/select_reference/<int:reference_id>", methods=["POST"])
def select_reference(reference_id):
    reference_dao.add_selected_reference(reference_id)
    selected_references = reference_dao.get_selected_references()
    refs = reference_dao.get_references()
    view_as_bibtex = reference_dao.get_reference_view_format()
    return render_template("reference_list.html", references=refs, view_as_bibtex=view_as_bibtex, selected_references=selected_references)

@app.route("/deselect_reference/<int:reference_id>", methods=["POST"])
def deselect_reference(reference_id):
    reference_dao.remove_from_selected(reference_id)
    selected_references = reference_dao.get_selected_references()
    refs = reference_dao.get_references()
    view_as_bibtex = reference_dao.get_reference_view_format()
    return render_template("reference_list.html", references=refs, view_as_bibtex=view_as_bibtex, selected_references=selected_references)
