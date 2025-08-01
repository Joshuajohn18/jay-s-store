def calculate_cart_total(cart, products_in_cart):
    total = 0
    for product in products_in_cart:
        product_id = str(product.id)
        quantity = int(cart.get(product_id, 0))  # Safer
        total += product.price * quantity       # Inside the loop
    return total
