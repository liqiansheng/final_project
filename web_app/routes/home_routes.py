# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")

@home_routes.route("/abbreviation")
def abbreviation():
    print("ABBREVIATION...")
    return render_template("abbreviation.html")

@home_routes.route("/definition.html")
def definition():
    print("DEFINITION...")
    return render_template("definition.html")

@home_routes.route("/definitions")
def definitions():
    print("DEFINITIONS...")
    return render_template("definitions.html")

