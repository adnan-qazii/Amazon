from ..extensions import db
from ..models import CartItem


def add_to_cart(user_id, product_id, quantity=1):
    existing_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if existing_item:
        existing_item.quantity += quantity
        db.session.commit()
        return existing_item
    item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
    db.session.add(item)
    db.session.commit()
    return item

def remove_from_cart(user_id, product_id):
    item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return True
    return False

def get_cart_items(user_id):
    return CartItem.query.filter_by(user_id=user_id).all()

