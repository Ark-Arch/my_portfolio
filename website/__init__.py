from flask import Flask


def create_web():
    web = Flask(__name__)
    web.config['SECRET_KEY'] = 'aisdhgnknihdgbv jd'

    from .routes import routes

    web.register_blueprint(routes, url_prefix='/')
    
    return web
