from ..extensions import db
from ..models import Product



def create_product(name, description, price, stock):
    """Create a new product"""
    product = Product(name=name, description=description, price=price, stock=stock)
    db.session.add(product)
    db.session.commit()
    return product

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def update_product(product, name=None, description=None, price=None, stock=None):
    """Update product details"""
    if name:
        product.name = name
    if description:
        product.description = description
    if price is not None:
        product.price = price
    if stock is not None:
        product.stock = stock
    db.session.commit()
    return product

def delete_product(product):
    db.session.delete(product)
    db.session.commit()
