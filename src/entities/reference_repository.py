# reference_repository.py
from config import db
from sqlalchemy import text

def get_references():
    """
    Hakee kaikki viitteet tietokannasta yhdellä optimoidulla kyselyllä.
    Returns:
        List[dict]: Lista viitteistä JSON-muodossa.
    """
    result = db.session.execute(text("""
        SELECT r.id, r.name, r.type, f.field_name, f.field_value, t.tag
        FROM references r
        LEFT JOIN fields f ON r.id = f.reference_id
        LEFT JOIN tags t ON r.id = t.reference_id
    """))

    references = {}
    for row in result.fetchall():
        ref_id = row[0]
        if ref_id not in references:
            references[ref_id] = {
                "id": ref_id,
                "name": row[1],
                "type": row[2],
                "fields": {},
                "tags": []
            }
        # Lisää kentät
        if row[3] and row[4]:
            references[ref_id]["fields"][row[3]] = row[4]
        # Lisää tägit
        if row[5]:
            references[ref_id]["tags"].append(row[5])

    return list(references.values())
