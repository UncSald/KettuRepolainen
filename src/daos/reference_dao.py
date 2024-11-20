from flask_sqlalchemy import SQLAlchemy

class ReferenceDao:
    def __init__(self, db_connection: SQLAlchemy):
        self.__db = db_connection

    