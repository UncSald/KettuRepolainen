from app import app, db
from sqlalchemy import text

def reset_db():
    tables = ["references"]
    for table_name in tables:
        print(f"Clearing contents from table {table_name}")
        sql = text(f"TRUNCATE TABLE \"references\";") # Täytyy muuttaa vastaamaan oikeaa tietokantapöytää lopuksi
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
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            journal TEXT,
            year INT NOT NULL,
            volume INT,
            number INT,
            pages INT,
            howpublished TEXT,
            month TEXT,
            note TEXT
        )
    """)
    db.session.execute(sql)
    db.session.commit()

def add_article_data(author, title, journal, year, volume, number, pages, month, note): 
    sql = text(
        "INSERT INTO article_data (author, title, journal, year, volume, number, pages, month, note) "
        "VALUES (:author, :title, :journal, :year, :volume, :number, :pages, :month, :note)"
    )
    db.session.execute(sql, {
        'author': author,
        'title': title,
        'journal': journal,
        'year': year,
        'volume': volume,
        'number': number,
        'pages': pages,
        'month': month, 
        'note': note
    })
    db.session.commit()

def add_misc_data(author, title, howpublished, month, year, note): 
    sql = text(
        "INSERT INTO misc_data (author, title, howpublished, month, year, note) "
        "VALUES (:author, :title, :howpublished, :month, :year, :note)"
    )
    db.session.execute(sql, {
        'author': author,
        'title': title,
        'howpublished': howpublished,
        'month':month,
        'year': year,
        'note': note
    })
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
