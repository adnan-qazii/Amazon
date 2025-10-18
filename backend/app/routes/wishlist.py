from flask import Blueprint, request, jsonify
from ..utils.decorators import token_required
from ..utils.wishlist import add_to_wishlist, remove_from_wishlist, get_wishlist_items

wishlist_bp = Blueprint("wishlist", __name__)



@wishlist_bp.route("/wishlist", methods=["GET"])
@token_required
def view_wishlist(current_user):
    items = get_wishlist_items(current_user.id)
    result = []
    for item in items:
        result.append({
            "product_id": item.product.id,
            "name": item.product.name,
            "price": item.product.price
        })
    return jsonify(result), 200

@wishlist_bp.route("/wishlist", methods=["POST"])
@token_required
def add_wishlist_item(current_user):
    data = request.get_json()
    product_id = data.get("product_id")
    if not product_id:
        return {"error": "Product ID is required"}, 400
    item = add_to_wishlist(current_user.id, product_id)
    return {"message": "Added to wishlist", "product_id": item.product_id}, 201



@wishlist_bp.route("/wishlist/<int:product_id>", methods=["DELETE"])
@token_required
def delete_wishlist_item(current_user, product_id):
    success = remove_from_wishlist(current_user.id, product_id)
    if success:
        return {"message": "Removed from wishlist"}, 200
    return {"error": "Item not found"}, 404
