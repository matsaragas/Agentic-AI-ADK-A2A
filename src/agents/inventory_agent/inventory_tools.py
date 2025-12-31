def get_inventory_info(product_name: str):

    """Get inventory information for a given product.

    Args:
        product_name: Name of the product (e.g., "iPhone 15 Pro", "MacBook Pro")

    Returns:
        inventory information as a string
    """
    # Mock product catalog - in production, this would query a real database
    product_catalog = {
        "iphone 15 pro": "Current Stock Quantity: 120, Location/Warehouse: London, Reserved Stock: 80, Supplier Name: Nikkon, Reorder Quantity: 200, Next Reorder Date: 2026-01-05",
        "samsung galaxy s24": "Current Stock Quantity: 20, Location/Warehouse: Lisbon, Reserved Stock: 10, Supplier Name: Samsung, Reorder Quantity: 100, Next Reorder Date: 2026-03-05",
        "dell xps 15": "Current Stock Quantity: 200, Location/Warehouse: Athens, Reserved Stock: 45, Supplier Name: Dell, Reorder Quantity: 300, Next Reorder Date: 2026-02-06",
        "macbook pro 14": "Current Stock Quantity: 50, Location/Warehouse: Rome, Reserved Stock: 20, Supplier Name: Apple, Reorder Quantity: 100, Next Reorder Date: 2026-03-05",
        "sony wh-1000xm5": "Current Stock Quantity: 60, Location/Warehouse: Madrid, Reserved Stock: 50, Supplier Name: Sony, Reorder Quantity: 120, Next Reorder Date: 2026-03-04",
        "ipad air": "Current Stock Quantity: 70, Location/Warehouse: Paris, Reserved Stock: 40, Supplier Name: Apple, Reorder Quantity: 130, Next Reorder Date: 2026-06-02",
        "lg ultrawide 34": "Current Stock Quantity: 80, Location/Warehouse: Tokyo, Reserved Stock: 30, Supplier Name: LG, Reorder Quantity: 140, Next Reorder Date: 2026-05-05",
    }

    product_lower = product_name.lower().strip()

    if product_lower in product_catalog:
        return f"Product: {product_catalog[product_lower]}"
    else:
        available = ", ".join([p.title() for p in product_catalog.keys()])
        return f"Sorry, I don't have information for {product_name}. Available products: {available}"
