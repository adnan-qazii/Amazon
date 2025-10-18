from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(auth_bp)

    return app
