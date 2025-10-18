from ..extensions import db
from ..models import User
from passlib.hash import argon2
import jwt
from datetime import datetime, timedelta
from flask import current_app


def get_user_by_email(email):
    """Return user object by email or None"""
    return User.query.filter_by(email=email).first()

def get_user_by_username(username):
    """Return user object by username or None"""
    return User.query.filter_by(username=username).first()

def create_user(username, email, password):
    """Create a new user with hashed password"""
    hashed_password = argon2.hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def verify_password(user, password):
    """Verify plain password against stored hash"""
    return argon2.verify(password, user.password)

def generate_jwt(user_id, hours=1):
    """Generate JWT token valid for 'hours' hours"""
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=hours)
    }
    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token
