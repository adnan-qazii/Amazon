from flask import Blueprint, request, jsonify
from ..utils.product import create_product, get_product_by_id, update_product, delete_product
from ..utils.decorators import token_required
from ..models.product import Product
from ..utils.decorators import admin_required

product_bp = Blueprint("product", __name__)


@product_bp.route("/products", methods=["GET"])
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


@product_bp.route("/products/<int:product_id>", methods=["GET"])
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
