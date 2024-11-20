from config import db, app
from sqlalchemy import text

def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )
    print(f"Checking if table {name} exists")
    print(sql_table_existence)
    result = db.session.execute(sql_table_existence)
    return result.fetchone()[0]

def reset_db():
    tables = ["reference_id", "article_data"]
    for table_name in tables:
        print(f"Clearing contents from table {table_name}")
        sql = text(f"DELETE FROM {table_name}")
        db.session.execute(sql)
    db.session.commit()

def setup_db():
    tables = ["reference_id", "article_data"]
    for table_name in tables:
        if table_exists(table_name):
            print(f"Table {table_name} exists, dropping")
            sql = text(f"DROP TABLE {table_name}")
            db.session.execute(sql)
    db.session.commit()

    print("Creating table reference_id")
    sql = text(
        "CREATE TABLE reference_id ("
        "  id SERIAL PRIMARY KEY, "
        "  type TEXT NOT NULL"
        ")"
    )
    db.session.execute(sql)
    db.session.commit()

    print("Creating table article_data")
    sql = text(
        "CREATE TABLE article_data ("
        "  id SERIAL PRIMARY KEY, "
        "  ref_id int REFERENCES reference_id (id), "
        "  name TEXT NOT NULL, "
        "  author TEXT NOT NULL, "
        "  title TEXT NOT NULL, "
        "  journal TEXT NOT NULL, "
        "  year INT NOT NULL, "
        "  volume TEXT NOT NULL, "
        "  number TEXT NOT NULL, "
        "  pages TEXT NOT NULL"
        ")"
    )
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
