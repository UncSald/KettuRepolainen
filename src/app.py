from flask import Flask, redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from entities.todo_repository import get_todos, create_todo, set_done
from config import app
from util import validate_todo
from entities.reference_creation import create_article_reference
from entities.reference_repository import get_references
from config import SECRET_KEY
from daos.reference_dao import ReferenceDao

app = Flask(__name__)
app.secret_key = SECRET_KEY

from db import db

reference_dao = ReferenceDao(db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new_reference():
    return render_template("new_reference.html")

@app.route("/references")
def reference_list():
    references = get_references()
    return render_template("reference_list.html", references=references)

@app.route("/create_reference", methods=["POST"])
def create_new_reference():
    name = request.form.get("name")
    author= request.form.get("author")
    title= request.form.get("title")
    journal= request.form.get("journal")
    year= request.form.get("year")
    volume= request.form.get("volume")
    number= request.form.get("number")
    pages= request.form.get("pages")
    create_article_reference(name,[author,title,journal,year,volume,number,pages])
    return redirect("/")
 
@app.route("/get_references", methods=["GET"])
def references():
    """
    Fetches all references from the database and returns them as a JSON response.
    Returns a 200 status with the references or a 500 status with an error message.
    """
    try:
        ref = get_references()   # Fetch references from the repository
        return jsonify(ref), 200   # Return references as JSON with a 200 status code
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error message if an exception occurs
