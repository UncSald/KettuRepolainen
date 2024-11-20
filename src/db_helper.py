from app import app, db
from sqlalchemy import text

def table_exists(name: str):
    sql = text
    """
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_name = :table_name
    )
    """
    
    print(f"Checking if table {name} exists")
    print(sql)
    result = db.session.execute(sql, {"table_name": name})
    return result.fetchone()[0]

def reset_db():
    tables = ["references"]
    for table_name in tables:
        print(f"Clearing contents from table {table_name}")
        sql = text(f"TRUNCATE TABLE {table_name}")
        db.session.execute(sql)
    db.session.commit()

def setup_db():
    tables = ["references"]
    for table_name in tables:
        if table_exists(table_name):
            print(f"Table {table_name} exists, dropping")
            sql = text(f"DROP TABLE {table_name}")
            db.session.execute(sql)
    db.session.commit()

    print("Creating table references")
    sql = text("""
        CREATE TABLE references (
            id SERIAL PRIMARY KEY,
            type TEXT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            journal TEXT,
            year INT NOT NULL,
            volume INT,
            number INT,
            pages INT
        )
    """)
    db.session.execute(sql)
    db.session.commit()

def add_article_data(author, title, journal, year, volume, number, pages):
    sql = text(
        "INSERT INTO article_data (author, title, journal, year, volume, number, pages) "
        "VALUES (:author, :title, :journal, :year, :volume, :number, :pages)"
    )
    db.session.execute(sql, {
        'author': author,
        'title': title,
        'journal': journal,
        'year': year,
        'volume': volume,
        'number': number,
        'pages': pages
    })
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
