from flask import Blueprint, request, jsonify
from ..utils.decorators import token_required
from ..utils.user import get_user_by_email, get_user_by_username, create_user, verify_password, generate_jwt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return {"error": "All fields are required"}, 400

    if get_user_by_username(username) or get_user_by_email(email):
        return {"error": "Username or email already exists"}, 400

    create_user(username, email, password)
    return {"message": "User registered successfully"}, 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email and password are required"}, 400

    user = get_user_by_email(email)
    if not user or not verify_password(user, password):
        return {"error": "Invalid email or password"}, 401

    token = generate_jwt(user.id)
    return {"token": token}, 200

@auth_bp.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "created_at": current_user.created_at
    }, 200
