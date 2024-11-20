from config import db
from sqlalchemy import text

def create_article_reference(data):
    """Add a new reference to the database.
    Add reference name to a table containing reference names.
    Connect reference name to a table containing its data.

    Args:
        data (dict): Author, title, journal, year, volume, number, and pages
        of the referenced article.
    """
    sql_reference_data=text("INSERT INTO references \
                                (name,author,title,journal,year,volume,number,pages)\
                                VALUES (:name,:author,:title,\
                                :journal,:year,:volume,:number,:pages)")
    db.session.execute(sql_reference_data,\
                           {"name":data["name"],"author":data["author"],"title":data["title"],
                                "journal":data["journal"],"year":data["year"],
                                "volume":data["volume"],"number":data["number"],
                                "pages":data["pages"]})
    db.session.commit()
