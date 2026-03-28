from flask import render_template, request, redirect, url_for
from app import app

users = []

@app.route("/", methods=["GET", "POST"])
def blog():
    if request.method == "POST":
        name = request.form["name"]
        town = request.form["town"]
        hobby = request.form["hobby"]
        age = request.form["age"]
        if name and hobby:
            users.append({
                "name": name,
                "town": town,
                "hobby": hobby,
                "age": age
            })

        return redirect(url_for("blog"))
    return render_template("blog.html", users=users)
