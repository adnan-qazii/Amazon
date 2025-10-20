from flask import Blueprint, jsonify, url_for, send_from_directory, current_app
from ..utils.product import  get_product_by_id

from ..models.product import Product


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
            "image": url_for('product.get_image', filename=p.image, _external=True) if p.image else None,
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
        "image": url_for('product.get_image', filename=product.image, _external=True) if product.image else None,
        "created_at": product.created_at,
        "updated_at": product.updated_at
    }, 200


@product_bp.route("/products/images/<filename>")
def get_image(filename):
    """Serve product images"""
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
