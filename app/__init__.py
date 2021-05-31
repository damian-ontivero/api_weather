'''
App configuration
'''

from flask import Flask, jsonify
from flask_restful import Api

from app.db import db
from app.common.error_handling import AppErrorBaseClass, ObjectNotFound
from config import Config
from app.weather.api.resources import weather_bp
from .ext import ma, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extension init
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Capture all 404 errors
    Api(app, catch_all_404s=True)

    # Disable strict slashes mode
    app.url_map.strict_slashes = False
    
    # Blueprint register
    app.register_blueprint(weather_bp)

    # Error handler register
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'message': 'Internal server error.'}), 500
    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'message': 'Method not allowed.'}), 405
    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'message': 'Forbidden error.'}), 403
    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'message': 'Not Found error.'}), 404
    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'message': str(e)}), 500
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'message': str(e)}), 404