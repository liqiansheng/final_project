# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template

from app.covid_lookup import get_covid_case

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

@home_routes.route("/covid/form")
def covid_form():
    print("WEATHER FORM...")
    return render_template("covid_form.html")

@home_routes.route("/covid/result", methods=["GET", "POST"])
def covid():
    print("Covid Cases...")
    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    user_input = request_data.get("state_abbrev") 

    results = get_covid_case(user_input)

        #flash("Weather Forecast Generated Successfully!", "success")
    return render_template("covid_result.html",user_input=user_input,results = results)
   

