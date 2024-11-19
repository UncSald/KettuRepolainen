from config import db
from sqlalchemy import text

def create_reference(name, data):
    """Add a new reference to the database.
    Add reference name to a table containing reference names.
    Connect reference name to a table containing its data.

    Args:
        name (str): Name of the reference
    """
    sql_create_reference=text("INSERT INTO reference_id (name) VALUES (:name)")
    sql_reference_data=text("INSERT INTO reference_data \
                            (ref_id,author,title,journal,year,volume,number,pages)\
                            VALUES (:ref_id,:author,:title,:journal,:year,:volume,:number,:pages)")
    db.session.execute(sql_create_reference, {"name": name})
    db.session.commit()
    id_sql = text("SELECT id FROM reference_id WHERE name=(:name)")
    id = db.session.execute(id_sql, {"name":name}).fetchone()[0]
    db.session.execute(sql_reference_data, {"ref_id":id,"author":data[0],"title":data[1],
                                            "journal":data[2],"year":data[3],
                                            "volume":data[4],"number":data[5],
                                            "pages":data[6]})
    db.session.commit()
    print(db.session.execute(text("SELECT * FROM reference_data")).fetchall())
