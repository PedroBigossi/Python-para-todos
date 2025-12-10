# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui-troque-depois'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

    from .routes import main
    app.register_blueprint(main)

    return app