from flask import Blueprint, request, jsonify
from ..utils.decorators import token_required
from ..utils.cart import add_to_cart, remove_from_cart, get_cart_items

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/cart", methods=["GET"])
@token_required
def view_cart(current_user):
    items = get_cart_items(current_user.id)
    result = []
    for item in items:
        result.append({
            "product_id": item.product.id,
            "name": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity
        })
    return jsonify(result), 200

@cart_bp.route("/cart", methods=["POST"])
@token_required
def add_cart_item(current_user):
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)
    if not product_id:
        return {"error": "Product ID is required"}, 400
    item = add_to_cart(current_user.id, product_id, quantity)
    return {"message": "Added to cart", "product_id": item.product_id, "quantity": item.quantity}, 201

@cart_bp.route("/cart/<int:product_id>", methods=["DELETE"])
@token_required
def delete_cart_item(current_user, product_id):
    success = remove_from_cart(current_user.id, product_id)
    if success:
        return {"message": "Removed from cart"}, 200
    return {"error": "Item not found"}, 404
