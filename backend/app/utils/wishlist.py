from ..extensions import db
from ..models import  WishlistItem


def add_to_wishlist(user_id, product_id):
    existing_item = WishlistItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if existing_item:
        return existing_item
    item = WishlistItem(user_id=user_id, product_id=product_id)
    db.session.add(item)
    db.session.commit()
    return item

def remove_from_wishlist(user_id, product_id):
    item = WishlistItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return True
    return False

def get_wishlist_items(user_id):
    return WishlistItem.query.filter_by(user_id=user_id).all()
