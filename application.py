import hmac
import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev-only-change-me")
PASSWORD = os.getenv("PAGE_PASSWORD")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        submitted_password = request.form.get("password", "")
        if PASSWORD and hmac.compare_digest(submitted_password, PASSWORD):
            session["authenticated"] = True
            return redirect(url_for("protected"))
        flash("Mot de passe incorrect.", "error")

    return render_template("login.html")


@app.route("/protected", methods=["GET", "POST"])
def protected():
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    if request.method == "POST":
        session["page_content"] = request.form.get("content", "")
        flash("Page mise a jour.", "success")

    content = session.get(
        "page_content",
        "Bienvenue sur votre page protegee. Modifiez ce texte, puis enregistrez-le.",
    )
    return render_template("protected.html", content=content)


# @app.get("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


@app.route('/maps')
def maps():
    return render_template('maps.html')


if __name__ == "__main__":
    app.run(debug=True)