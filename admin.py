from flask import request, redirect, url_for
from database import get_db

# ----------------- PRODUITS -----------------


def add_product():
    name = request.form["name"]
    boycotted = int(request.form["boycotted"])
    alternative = request.form.get("alternative", "")

    db = get_db()
    db.execute(
        "INSERT OR IGNORE INTO products (name, boycotted, alternative) VALUES (?, ?, ?)",
        (name, boycotted, alternative),
    )
    db.commit()
    db.close()
    return redirect(url_for("admin_dashboard"))


def update_product(product_id):
    boycotted = int(request.form["boycotted"])
    alternative = request.form.get("alternative", "")

    db = get_db()
    db.execute(
        "UPDATE products SET boycotted=?, alternative=? WHERE id=?",
        (boycotted, alternative, product_id),
    )
    db.commit()
    db.close()
    return redirect(url_for("admin_dashboard"))


def delete_product(product_id):
    db = get_db()
    db.execute("DELETE FROM products WHERE id=?", (product_id,))
    db.commit()
    db.close()
    return redirect(url_for("admin_dashboard"))


# ----------------- LIEUX -----------------


def add_location():
    name = request.form["name"]
    alt_name = request.form["alt_name"]

    db = get_db()
    db.execute(
        "INSERT OR IGNORE INTO locations (name, alt_name) VALUES (?, ?)",
        (name, alt_name),
    )
    db.commit()
    db.close()
    return redirect(url_for("admin_dashboard"))


def update_location(location_id):
    name = request.form["name"]
    alt_name = request.form["alt_name"]

    db = get_db()
    db.execute(
        "UPDATE locations SET name=?, alt_name=? WHERE id=?",
        (name, alt_name, location_id),
    )
    db.commit()
    db.close()
    return redirect(url_for("admin_dashboard"))


def delete_location(location_id):
    db = get_db()
    db.execute("DELETE FROM locations WHERE id=?", (location_id,))
    db.commit()
    db.close()
    return redirect(url_for("admin_dashboard"))
