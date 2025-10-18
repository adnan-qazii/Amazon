from flask import Blueprint, jsonify
from ..utils.decorators import token_required
from ..utils.order import checkout_cart, get_user_orders

order_bp = Blueprint("order", __name__)




@order_bp.route("/checkout", methods=["POST"])
@token_required
def checkout(current_user):
    order, error = checkout_cart(current_user.id)
    if error:
        return {"error": error}, 400
    return {"message": "Order placed successfully", "order_id": order.id}, 201




@order_bp.route("/orders", methods=["GET"])
@token_required
def list_orders(current_user):
    orders = get_user_orders(current_user.id)
    result = []
    for o in orders:
        items = []
        for i in o.items:
            items.append({
                "product_id": i.product.id,
                "name": i.product.name,
                "quantity": i.quantity,
                "price": i.price
            })
        result.append({
            "order_id": o.id,
            "total_price": o.total_price,
            "status": o.status,
            "created_at": o.created_at,
            "items": items
        })
    return jsonify(result), 200
