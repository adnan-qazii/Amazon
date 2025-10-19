from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes import auth_bp
from .routes.product import product_bp
from .routes.cart import cart_bp
from .routes.wishlist import wishlist_bp    
from .routes.order import order_bp
from .routes.admin import admin_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(wishlist_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(admin_bp)

    return app
