from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
DATABASE_URL = getenv("DATABASE_URL")

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
