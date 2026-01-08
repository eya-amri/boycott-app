from flask import Flask, render_template, request, session, redirect, url_for
from database import init_db, get_db
from auth import signup_user, login_user, logout_user
from boycott import check_product, check_location
from admin import (
    add_product,
    update_product,
    delete_product,
    add_location,
    update_location,
    delete_location,
)

app = Flask(__name__)
app.secret_key = "secret"

# ----------------- USER ROUTES -----------------


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return signup_user()
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return login_user()
    return render_template("login.html")


@app.route("/logout")
def logout():
    return logout_user()


@app.route("/check", methods=["GET", "POST"])
def check():
    if "user" not in session:
        return redirect(url_for("login"))

    result = None
    if request.method == "POST":
        check_type = request.form.get("check_type")
        name = request.form.get("name")
        if check_type == "product":
            result = check_product(name)
        elif check_type == "location":
            result = check_location(name)

    return render_template("check.html", result=result)


# ----------------- ADMIN LOGIN -----------------


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        db = get_db()
        admin = db.execute(
            "SELECT * FROM users WHERE username=? AND role='admin'", (username,)
        ).fetchone()
        db.close()

        if admin and admin[2] == password:  # index 2 = password
            session["user"] = admin[1]  # index 1 = username
            session["role"] = admin[3]  # index 3 = role
            return redirect(url_for("admin_dashboard"))
        else:
            error = "Invalid admin username or password"

    return render_template("admin_login.html", error=error)


# ----------------- ADMIN DASHBOARD -----------------


@app.route("/admin/dashboard")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect(url_for("admin_login"))

    db = get_db()
    products = db.execute(
        "SELECT id, name, boycotted, alternative FROM products"
    ).fetchall()
    locations = db.execute("SELECT id, name, alt_name FROM locations").fetchall()
    db.close()

    return render_template(
        "admin_dashboard.html", products=products, locations=locations
    )


# ----------------- PRODUCT CRUD -----------------


@app.route("/admin/add_product", methods=["POST"])
def route_add_product():
    if session.get("role") != "admin":
        return redirect(url_for("admin_login"))
    return add_product()


@app.route("/admin/update_product/<int:product_id>", methods=["POST"])
def route_update_product(product_id):
    if session.get("role") != "admin":
        return redirect(url_for("admin_login"))
    return update_product(product_id)


@app.route("/admin/delete_product/<int:product_id>")
def route_delete_product(product_id):
    if session.get("role") != "admin":
        return redirect(url_for("admin_login"))
    return delete_product(product_id)


# ----------------- LOCATION CRUD -----------------


@app.route("/admin/add_location", methods=["POST"])
def route_add_location():
    if session.get("role") != "admin":
        return redirect(url_for("admin_login"))
    return add_location()


@app.route("/admin/update_location/<int:location_id>", methods=["POST"])
def route_update_location(location_id):
    if session.get("role") != "admin":
        return redirect(url_for("admin_login"))
    return update_location(location_id)


@app.route("/admin/delete_location/<int:location_id>")
def route_delete_location(location_id):
    if session.get("role") != "admin":
        return redirect(url_for("admin_login"))
    return delete_location(location_id)


# ----------------- RUN APP -----------------

if __name__ == "__main__":
    init_db()
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
