from flask import Flask, render_template, request, redirect, url_for, session
from auth import register_user, login_user
from database import create_table

# test

app.secret_key = "super_secret_key"

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        message = register_user(username, password)
        return render_template("register.html", message=message)

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        success, message = login_user(username, password)

        if "user" in session:
            return redirect(url_for("dashboard"))

        return render_template("login.html", message=message)

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["user"]
    )

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)