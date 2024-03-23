from flask import Blueprint, render_template, send_from_directory


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template("home_page.html")

@routes.route('/my-projects')
def my_projects():
    return render_template("my_projects.html")

@routes.route('/fun-gallery')
def fun_gallery():
    return render_template("fun_gallery.html")

@routes.route('/my-skills')
def my_skills():
    return render_template("my_skills.html")

@routes.route('/download/resume')
def download_resume():
    return send_from_directory('static', "david_agbemuko_c.v.docx", as_attachment=True)

