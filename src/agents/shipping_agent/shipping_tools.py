def get_shipping_info(product_name: str):

    """Get shipping information for a given product.

    Args:
        product_name: Name of the product (e.g., "iPhone 15 Pro", "MacBook Pro")

    Returns:
        shipping information as a string
    """
    # Mock product catalog - in production, this would query a real database
    product_catalog = {
        "iphone 15 pro": "iphone 15 pro can be delivered in 15 days",
        "samsung galaxy s24": "samsung galaxy s24 can be delivered in 12 days",
        "dell xps 15": 'dell xps 15 can be delivered in 20 days',
        "macbook pro 14": 'macbook pro 14 can be delivered in 25 days',
        "sony wh-1000xm5": "Sony WH-1000XM5 Headphones available in 25 days",
        "ipad air": 'iPad Air, can be delivered in 12 days, $15 extra delivery costs',
        "lg ultrawide 34": 'LG UltraWide 34" can be delivered in 25 days, no extra delivery cost',
    }

    product_lower = product_name.lower().strip()

    if product_lower in product_catalog:
        return f"Product: {product_catalog[product_lower]}"
    else:
        available = ", ".join([p.title() for p in product_catalog.keys()])
        return f"Sorry, I don't have information for {product_name}. Available products: {available}"
