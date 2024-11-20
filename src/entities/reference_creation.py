from config import db
from sqlalchemy import text

def create_article_reference(name, data):
    """Add a new reference to the database.
    Add reference name to a table containing reference names.
    Connect reference name to a table containing its data.

    Args:
        name (str): Name of the reference.
        data (list): Author, title, journal, year, volume, number, and pages
        of the referenced article.
    """
    if reference_exists(name):
        id_sql = text("SELECT id FROM reference_id WHERE name=(:name)")
        id = db.session.execute(id_sql, {"name":name}).fetchone()[0]
        db.session.execute(sql_reference_data,\
                           {"ref_id":id,"author":data[0],"title":data[1],
                                "journal":data[2],"year":data[3],
                                "volume":data[4],"number":data[5],
                                "pages":data[6]})
    else:
        sql_create_reference=text("INSERT INTO reference_id (name) VALUES (:name)")
        sql_reference_data=text("INSERT INTO reference_data \
                                (ref_id,author,title,journal,year,volume,number,pages)\
                                VALUES (:ref_id,:author,:title,\
                                :journal,:year,:volume,:number,:pages)")
        db.session.execute(sql_create_reference, {"name": name})
        db.session.commit()
        id_sql = text("SELECT id FROM reference_id WHERE name=(:name)")
        id = db.session.execute(id_sql, {"name":name}).fetchone()[0]
        db.session.execute(sql_reference_data,\
                           {"ref_id":id,"author":data[0],"title":data[1],
                                "journal":data[2],"year":data[3],
                                "volume":data[4],"number":data[5],
                                "pages":data[6]})
    db.session.commit()




def reference_exists(name):
    """Checks if a reference exists in the database.

    Args:
        name (str): Name of the reference.

    Returns:
        Bool: True if the reference already exists in the database,
        else: False.
    """
    sql_existing = text("SELECT name FROM reference_id where name=(:name)")
    result = db.session.execute(sql_existing, {"name":name}).fetchone()
    return result != None
