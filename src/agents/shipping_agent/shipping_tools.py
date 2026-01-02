def get_shipping_info(product_name: str):

    """Get shipping information for a given product.

    Args:
        product_name: Name of the product (e.g., "iPhone 15 Pro", "MacBook Pro")

    Returns:
        shipping information as a string
    """
    # Mock product catalog - in production, this would query a real database
    product_catalog = {
        "iphone 15 pro": "iphone 15 pro can be delivered in 15 days, shipping cost is $9.99. Express shipping in 2-3 business days with cost $20.",
        "samsung galaxy s24": "samsung galaxy s24 can be delivered in 12 days, shipping cost is $19.99. Express shipping in 1-2 business days with cost $25.",
        "dell xps 15": 'dell xps 15 can be delivered in 20 days, shipping cost is $5.99. Express shipping in 1-2 business days with cost $15.',
        "macbook pro 14": 'macbook pro 14 can be delivered in 25 days, shipping cost is $1.99. Express shipping in 1-2 business days with cost $5.',
        "sony wh-1000xm5": "Sony WH-1000XM5 Headphones available in 25 days, shipping cost is $4.99. Express shipping in 5-6 business days with cost $35.",
        "ipad air": 'iPad Air, can be delivered in 12 days, $15 extra delivery costs, shipping cost is $0.99. Express shipping in 1-2 business days with cost $2.5',
        "lg ultrawide 34": 'LG UltraWide 34" can be delivered in 25 days, no extra delivery cost. No shipping costs and express shipping available.',
    }

    product_lower = product_name.lower().strip()

    if product_lower in product_catalog:
        return f"Product: {product_catalog[product_lower]}"
    else:
        available = ", ".join([p.title() for p in product_catalog.keys()])
        return f"Sorry, I don't have information for {product_name}. Available products: {available}"
