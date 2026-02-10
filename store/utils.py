from django.contrib.auth.hashers import make_password, check_password

def hash_password(password):
    """Hash a password for storing."""
    return make_password(password)

def verify_password(plain_password, hashed_password):
    """Verify a stored password against one provided by user."""
    return check_password(plain_password, hashed_password)

def calculate_cart_total(cart_items):
    """Calculate total from cart items."""
    return sum(item.total for item in cart_items)

def calculate_order_total(subtotal, shipping=50):
    """Calculate order total with shipping."""
    return subtotal + shipping
