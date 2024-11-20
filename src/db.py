from app import app
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URL

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
