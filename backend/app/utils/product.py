from ..extensions import db
from ..models import Product
import os
from werkzeug.utils import secure_filename
from flask import current_app


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def save_product_image(file):
    """Save uploaded image and return filename"""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Create unique filename to avoid conflicts
        import uuid
        unique_filename = f"{uuid.uuid4()}_{filename}"
        
        # Ensure upload directory exists
        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        
        # Save file
        filepath = os.path.join(upload_folder, unique_filename)
        file.save(filepath)
        return unique_filename
    return None


def delete_product_image(image_filename):
    """Delete product image from filesystem"""
    if image_filename:
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename)
        if os.path.exists(filepath):
            os.remove(filepath)


def create_product(name, description, price, stock, image=None):
    """Create a new product"""
    product = Product(name=name, description=description, price=price, stock=stock, image=image)
    db.session.add(product)
    db.session.commit()
    return product


def get_product_by_id(product_id):
    return Product.query.get(product_id)


def update_product(product, name=None, description=None, price=None, stock=None, image=None):
    """Update product details"""
    if name:
        product.name = name
    if description:
        product.description = description
    if price is not None:
        product.price = price
    if stock is not None:
        product.stock = stock
    if image is not None:
        # Delete old image if exists
        if product.image:
            delete_product_image(product.image)
        product.image = image
    db.session.commit()
    return product


def delete_product(product):
    # Delete associated image
    if product.image:
        delete_product_image(product.image)
    db.session.delete(product)
    db.session.commit()
