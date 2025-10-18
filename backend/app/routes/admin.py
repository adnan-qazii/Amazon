from flask import Blueprint, request, jsonify
from ..utils.product import create_product, get_product_by_id, update_product, delete_product
from ..utils.decorators import token_required
from ..models.product import Product
from ..utils.decorators import admin_required
from utils.admin import get_all_users, get_all_orders, get_admin_stats

admin_bp = Blueprint("admin", __name__)

# ----------------------------
# Public Routes
# ----------------------------

@admin_bp.route("/products", methods=["GET"])
def list_products():
    products = Product.query.all()
    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "stock": p.stock,
            "created_at": p.created_at,
            "updated_at": p.updated_at
        })
    return jsonify(result), 200

@admin_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"error": "Product not found"}, 404
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
        "created_at": product.created_at,
        "updated_at": product.updated_at
    }, 200

# ----------------------------
# Admin Routes (protected)
# ----------------------------

@admin_bp.route("/products", methods=["POST"])
@token_required
@admin_required
def create_product_route(current_user):
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    if not name or price is None or stock is None:
        return {"error": "Name, price, and stock are required"}, 400

    product = create_product(name, description, price, stock)
    return {"message": "Product created", "id": product.id}, 201



@admin_bp.route("/products/<int:product_id>", methods=["PUT"])
@token_required
@admin_required
def update_product_route(current_user, product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"error": "Product not found"}, 404

    data = request.get_json()
    product = update_product(product,
    name=data.get("name"),
    description=data.get("description"),
    price=data.get("price"),
    stock=data.get("stock"))
    return {"message": "Product updated"}, 200




@admin_bp.route("/products/<int:product_id>", methods=["DELETE"])
@token_required
@admin_required
def delete_product_route(current_user, product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"error": "Product not found"}, 404
    delete_product(product)
    return {"message": "Product deleted"}, 200




@admin_bp.route("/admin/users", methods=["GET"])
@token_required
@admin_required
def get_users(current_user):
    users = get_all_users()
    result = []
    for u in users:
        result.append({
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "role": u.role,
            "created_at": u.created_at
        })
    return jsonify(result), 200


@admin_bp.route("/admin/orders", methods=["GET"])
@token_required
@admin_required
def get_orders(current_user):
    orders = get_all_orders()
    result = []
    for o in orders:
        result.append({
            "id": o.id,
            "user_id": o.user_id,
            "total_price": o.total_price,
            "status": o.status,
            "created_at": o.created_at
        })
    return jsonify(result), 200


@admin_bp.route("/admin/stats", methods=["GET"])
@token_required
@admin_required
def get_stats(current_user):
    stats = get_admin_stats()
    return jsonify(stats), 200