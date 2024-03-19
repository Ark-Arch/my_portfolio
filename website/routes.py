from flask import Blueprint, render_template


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template("home_page.html")

@routes.route('/my-projects')
def my_projects():
    return render_template("my_projects.html")



