from sqlalchemy import text
from config import db
from config import app


def reset_db():

    sql = text("TRUNCATE TABLE \"references\";")
    db.session.execute(sql)
    db.session.commit()
    add_default_input()

def setup_db():

    sql = text(f"DROP TABLE IF EXISTS \"references\" CASCADE;")
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
    add_default_input()

def add_default_input():
    data_c_book = ["book", "K&R1978",
                   "Kernighan, Brian and Ritchie, Dennis",
                   "The C Programming Language", None,
                   1978, None, None, None, None, None,
                   None, None, "Prentice Hall" ]
    data_flask_misc = ["misc", "Flask3.1", "Open source", "Flask 3.1.0 Documentation",
                       None, 2024, None, None,None,None,None,None,None,None]
    reference_sql = text("""
            INSERT INTO \"references\" (
                type,name,author,title,journal,year,volume,number,pages, month, note, howpublished, editor, publisher
            )                
            VALUES (
                :type, :name, :author, :title, :journal,:year,:volume,:number,:pages, :month, :note, :howpublished, :editor, :publisher
            )
        """)
    db.session.execute(reference_sql,{
                        "type":data_c_book[0],
                "name":data_c_book[1],
                "author":data_c_book[2],
                "title":data_c_book[3],
                "journal":data_c_book[4],
                "year":data_c_book[5],
                "volume":data_c_book[6],
                "number":data_c_book[7],
                "pages":data_c_book[8],
                "month":data_c_book[9],
                "note":data_c_book[10],
                "howpublished":data_c_book[11],
                "editor":data_c_book[12],
                "publisher":data_c_book[13]
                })
    db.session.execute(reference_sql,{
                        "type":data_flask_misc[0],
                "name":data_flask_misc[1],
                "author":data_flask_misc[2],
                "title":data_flask_misc[3],
                "journal":data_flask_misc[4],
                "year":data_flask_misc[5],
                "volume":data_flask_misc[6],
                "number":data_flask_misc[7],
                "pages":data_flask_misc[8],
                "month":data_flask_misc[9],
                "note":data_flask_misc[10],
                "howpublished":data_flask_misc[11],
                "editor":data_flask_misc[12],
                "publisher":data_flask_misc[13]
                })
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
