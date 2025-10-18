from ..extensions import db
from ..models import Order, OrderItem, CartItem



def checkout_cart(user_id):
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    if not cart_items:
        return None, "Cart is empty"

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order(user_id=user_id, total_price=total_price)
    db.session.add(order)
    db.session.flush()  # get order.id before committing

    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )
        db.session.add(order_item)
        # optionally reduce stock
        item.product.stock -= item.quantity
        db.session.delete(item)  # remove from cart

    db.session.commit()
    return order, None

def get_user_orders(user_id):
    return Order.query.filter_by(user_id=user_id).all()
