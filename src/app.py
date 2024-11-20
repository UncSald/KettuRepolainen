from flask import redirect, render_template, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy

from daos.reference_dao import ReferenceDao
from config import app, db

reference_dao = ReferenceDao(db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new_reference():
    return render_template("/new_reference.html")
 
@app.route("/references", methods=["GET"])
def references():
    """
    Fetches all references from the database and returns them as a JSON response.
    Returns a 200 status with the references or a 500 status with an error message.
    """

    refs = reference_dao.get_references()   # Fetch references from the repository
    return render_template("reference_list.html", references=refs)



@app.route("/references", methods=["POST"])
def create_new_reference():
    data = {}
    data["name"] = request.form.get("name")
    data["author"] = request.form.get("author")
    data["title"] = request.form.get("title")
    data["journal"] = request.form.get("journal")
    data["year"] = request.form.get("year")
    data["volume"] = request.form.get("volume")
    data["number"] = request.form.get("number")
    data["pages"] = request.form.get("pages")

    reference_dao.create_reference(data)
    return redirect("/")
