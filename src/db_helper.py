from sqlalchemy import text
from config import db


def reset_db():
    tables = ["references"]
    for table_name in tables:
        print(f"Clearing contents from table {table_name}")
        sql = text("TRUNCATE TABLE \"references\";")
        db.session.execute(sql)
    db.session.commit()

def setup_db():
    tables = ["references"]
    for table_name in tables:
        print(f"Table {table_name} exists, dropping")
        sql = text(f"DROP TABLE IF EXISTS \"{table_name}\" CASCADE;")
        db.session.execute(sql)
    db.session.commit()

    print("Creating table references")
    sql = text("""
        CREATE TABLE \"references\" (
            id SERIAL PRIMARY KEY,
            type TEXT,
            name TEXT NOT NULL,
            author TEXT,
            title TEXT,
            journal TEXT,
            year INT,
            volume INT,
            number INT,
            pages TEXT,
            howpublished TEXT,
            month TEXT,
            note TEXT,
            editor TEXT,
            link TEXT,
            publisher TEXT
        )
    """)
    db.session.execute(sql)
    db.session.commit()
