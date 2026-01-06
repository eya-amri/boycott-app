from flask import request, redirect, url_for, session
from database import get_db


def signup_user():
    db = get_db()
    db.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, 'user')",
        (request.form["username"], request.form["password"]),
    )
    db.commit()
    return redirect(url_for("login"))


def login_user():
    username = request.form["username"]
    password = request.form["password"]

    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE username=? AND password=?", (username, password)
    ).fetchone()

    if user:
        session["user"] = username
        session["role"] = user[3]

        if user[3] == "admin":
            return redirect(url_for("admin_dashboard"))
        return redirect(url_for("check"))

    return "Invalid credentials"


def logout_user():
    session.clear()
    return redirect(url_for("home"))
