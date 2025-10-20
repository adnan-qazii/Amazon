from flask import Blueprint, request, jsonify
from ..utils.product import create_product, get_product_by_id, update_product, delete_product, save_product_image
from ..models.product import Product
from ..utils.decorators import admin_required
from ..utils.admin import get_all_users, get_all_orders, get_admin_stats

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/products", methods=["POST"])
@admin_required
def create_product_route(current_user):
    # Check if request contains files (multipart/form-data)
    if 'image' in request.files:
        # Form data with file upload
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        stock = request.form.get("stock")
        image_file = request.files.get("image")
        
        # Save image
        image_filename = save_product_image(image_file) if image_file else None
    else:
        # JSON data without file
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        stock = data.get("stock")
        image_filename = None

    if not name or price is None or stock is None:
        return {"error": "Name, price, and stock are required"}, 400

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        return {"error": "Invalid price or stock value"}, 400

    product = create_product(name, description, price, stock, image=image_filename)
    return {"message": "Product created", "id": product.id}, 201



@admin_bp.route("/products/<int:product_id>", methods=["PUT"])
@admin_required
def update_product_route(current_user, product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"error": "Product not found"}, 404

    # Check if request contains files (multipart/form-data)
    if 'image' in request.files:
        # Form data with file upload
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        stock = request.form.get("stock")
        image_file = request.files.get("image")
        
        # Save new image
        image_filename = save_product_image(image_file) if image_file else None
    else:
        # JSON data without file
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        stock = data.get("stock")
        image_filename = None

    # Convert types if provided
    if price is not None:
        try:
            price = float(price)
        except ValueError:
            return {"error": "Invalid price value"}, 400
    
    if stock is not None:
        try:
            stock = int(stock)
        except ValueError:
            return {"error": "Invalid stock value"}, 400

    product = update_product(product,
        name=name,
        description=description,
        price=price,
        stock=stock,
        image=image_filename)
    return {"message": "Product updated"}, 200




@admin_bp.route("/products/<int:product_id>", methods=["DELETE"])
@admin_required
def delete_product_route(current_user, product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"error": "Product not found"}, 404
    delete_product(product)
    return {"message": "Product deleted"}, 200




@admin_bp.route("/users", methods=["GET"])
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


@admin_bp.route("/orders", methods=["GET"])
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



@admin_bp.route("/stats", methods=["GET"])
@admin_required
def get_stats(current_user):
    stats = get_admin_stats()
    return jsonify(stats), 200