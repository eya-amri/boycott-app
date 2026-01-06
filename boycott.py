from database import get_db


# ----------------- PRODUCT CHECK -----------------
def check_product(name):
    """
    Check if a product is boycotted and return its details.
    """
    db = get_db()
    # Use LIKE for partial match, case-insensitive
    product = db.execute(
        """
        SELECT p.name, p.boycotted, p.alternative
        FROM products p
        WHERE p.name LIKE ?
        LIMIT 1
    """,
        (f"%{name}%",),
    ).fetchone()
    db.close()

    if not product:
        return {"status": "not_found"}  

    return {
        "type": "Product",
        "name": product[0],
        "boycotted": bool(product[1]),
        "alternative": product[2],
    }


# ----------------- LOCATION CHECK -----------------
def check_location(name):
    """
    Check if a location is boycotted and return its details.
    """
    db = get_db()
    location = db.execute(
        """
        SELECT name, alt_name
        FROM locations
        WHERE name LIKE ?
        LIMIT 1
    """,
        (f"%{name}%",),
    ).fetchone()
    db.close()

    if not location:
        return {"status": "not_found"}  # Location not found

    return {
        "type": "Location",
        "name": location[0],
        "boycotted": True,  # Considered boycotted if listed
        "alternatives": "",
        "location": location[0],
        "alt_location": location[1],
    }
