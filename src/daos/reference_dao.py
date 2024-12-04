from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from ref_enum import Reference

class ReferenceDao:
    def __init__(self, db_connection: SQLAlchemy):
        self.__db = db_connection
        self.___references_in_bibtex_form: bool = False

    def change_reference_view_format(self):
        self.___references_in_bibtex_form = not self.___references_in_bibtex_form

    def get_reference_view_format(self):
        return self.___references_in_bibtex_form

    def create_reference(self, data):
        """Add a new reference to the database.
        Add reference name to a table containing reference names.
        Connect reference name to a table containing its data.

        Args:
            data (dict): Author, title, journal, year, volume, number, and pages
            of the referenced article.
        """

        sql = text("""
            INSERT INTO \"references\" (
                type,name,author,title,journal,year,volume,number,pages, month, note, howpublished, editor, publisher
            )                
            VALUES (
                :type, :name, :author, :title, :journal,:year,:volume,:number,:pages, :month, :note, :howpublished, :editor, :publisher
            )
        """)

        self.__db.session.execute(
            sql,
            {
                "type":data["type"],
                "name":data["name"],
                "author":data["author"],
                "title":data["title"],
                "journal":data["journal"],
                "year":data["year"],
                "volume":data["volume"],
                "number":data["number"],
                "pages":data["pages"],
                "month":data["month"],
                "note":data["note"],
                "howpublished":data["howpublished"],
                "editor":data["editor"],
                "publisher":data["publisher"]
            }
        )
        self.__db.session.commit()

    def get_references(self):
        """
        Hakee kaikki viitteet tietokannasta yhdellä optimoidulla kyselyllä.
        Returns:
            List[dict]: Lista viitteistä JSON-muodossa.
        """
        sql = text("""
            SELECT 
                id, type, name, author, title, journal, year, volume, number, pages, month, note, howpublished, editor, publisher
            FROM 
                \"references\"
        """)
        result = self.__db.session.execute(sql).fetchall()

        return result


    def get_reference(self, reference_id):
        sql = text("""
            SELECT 
                id, type, name, author, title, journal, year, volume, number, pages, month, note, howpublished, editor, publisher
            FROM 
                \"references\"
            WHERE
                id=:id
        """)

        result = self.__db.session.execute(sql, {"id":reference_id}).fetchone()
        return result
    
    def get_all_names(self):
        sql = text("""
            SELECT 
                   name
            FROM 
                \"references\"
        """)

        result = self.__db.session.execute(sql).fetchall()
        all_names = [i[0] for i in result]
        return all_names


    def update_reference(self, data):
        sql = text("""
            UPDATE
                \"references\" 
            SET 
                name=:name, 
                author=:author, 
                title=:title, 
                journal=:journal, 
                year=:year, 
                volume=:volume, 
                number=:number, 
                pages=:pages, 
                month=:month, 
                note=:note, 
                howpublished=:howpublished, 
                editor=:editor, 
                publisher=:publisher
            WHERE
                id=:id
        """)

        self.__db.session.execute(
            sql,
            {
                "id":data["id"],
                "type":data["type"],
                "name":data["name"],
                "author":data["author"],
                "title":data["title"],
                "journal":data["journal"],
                "year":data["year"],
                "volume":data["volume"],
                "number":data["number"],
                "pages":data["pages"],
                "month":data["month"],
                "note":data["note"],
                "howpublished":data["howpublished"],
                "editor":data["editor"],
                "publisher":data["publisher"]
            }
        )
        self.__db.session.commit()



    def return_references_in_bibtex_form(self):
        references = self.get_references()
        bibtex_data = ""
        for ref in references:
            ref_data = f"@{ref[Reference.TYPE.value]}""{"f"{ref[Reference.NAME.value]}"
            ref_data += f',\n  author       = "{ref[Reference.AUTHOR.value]}"'
            if ref[Reference.TITLE.value]:
                ref_data += f',\n  title        = "{ref[Reference.TITLE.value]}"'
            if ref[Reference.JOURNAL.value]:
                ref_data += f',\n  journal      = "{ref[Reference.JOURNAL.value]}"'
            if ref[Reference.YEAR.value]:
                ref_data += f',\n  year         = {ref[Reference.YEAR.value]}'
            if ref[Reference.VOLUME.value]:
                ref_data += f',\n  volume       = "{ref[Reference.VOLUME.value]}"'
            if ref[Reference.NUMBER.value]:
                ref_data += f',\n  number       = "{ref[Reference.NUMBER.value]}"'
            if ref[Reference.PAGES.value]:
                ref_data += f',\n  pages        = "{ref[Reference.PAGES.value]}"'
            if ref[Reference.MONTH.value]:
                ref_data += f',\n  month        = "{ref[Reference.MONTH.value]}"'
            if ref[Reference.NOTE.value]:
                ref_data += f',\n  note         = "{ref[Reference.NOTE.value]}"'
            if ref[Reference.HOWPUBLISHED.value]:
                ref_data += f',\n  howpublished = "{ref[Reference.HOWPUBLISHED.value]}"'
            if ref[Reference.EDITOR.value]:
                ref_data += f',\n  editor       = "{ref[Reference.EDITOR.value]}"'
            if ref[Reference.PUBLISHER.value]:
                ref_data += f',\n  publisher    = "{ref[Reference.PUBLISHER.value]}"'
            bibtex_data += ref_data+"\n}\n\n"
        return bibtex_data
    def delete_reference(self, reference_id):
        sql = text("""
            DELETE FROM "references"
            WHERE id = :id
        """)
        self.__db.session.execute(sql, {"id": reference_id})
        self.__db.session.commit()


