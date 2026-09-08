def price_alert(product_name, current_price, target_price):
    if current_price <= target_price:
        print("\n🔔 PRICE ALERT!")
        print("Product:", product_name)
        print("Current Price: ₹", current_price)
        print("Target Price: ₹", target_price)
        print("Buy now! Price is below your target.\n")
        return True

    return False