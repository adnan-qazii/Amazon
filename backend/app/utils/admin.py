from ..models import User, Order, Product
from ..extensions import db

# ----------------------------
# Admin Helper Functions
# ----------------------------

def get_all_users():
    """Return all registered users"""
    return User.query.all()


def get_all_orders():
    """Return all orders in the system"""
    return Order.query.all()


def get_admin_stats():
    """Return summary analytics"""
    total_users = User.query.count()
    total_products = Product.query.count()
    total_orders = Order.query.count()

    total_revenue = db.session.query(db.func.sum(Order.total_price)).scalar() or 0

    return {
        "total_users": total_users,
        "total_products": total_products,
        "total_orders": total_orders,
        "total_revenue": total_revenue
    }
