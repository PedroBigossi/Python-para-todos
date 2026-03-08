# app/__init__.py
import os
import logging
from flask import Flask, jsonify

logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    # SECRET_KEY must be set (e.g. via env); use a default only for local dev
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-in-production')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

    from .routes import main
    app.register_blueprint(main)

    @app.errorhandler(Exception)
    def handle_error(e):
        logger.exception("Unhandled error")
        return jsonify(error="Internal Server Error"), 500

    return app