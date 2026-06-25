from .models import Product


def calculate_relevance(product, query):
    """
    Returns:
        score (float)
        reason (str)
    """

    query = query.lower().strip()

    category = product.category.lower()

    name = product.product_name.lower()

    description = product.product_description.lower()

    tags = [tag.strip().lower() for tag in product.tags.split(",")]

    # --------------------------
    # Tier 1 : Category Match
    # --------------------------

    normalized_category = category.rstrip("s")

    if query == normalized_category:
        return 1.0, "Category Match"

    if query in category:
        return 0.95, "Category Partial Match"

    # --------------------------
    # Tier 2 : Tag Match
    # --------------------------

    if query in tags:
        return 0.80, "Exact Tag Match"

    for tag in tags:
        if query in tag:
            return 0.70, "Partial Tag Match"

    # --------------------------
    # Tier 3 : Product Name
    # --------------------------

    if query in name:
        return 0.60, "Product Name Match"

    # --------------------------
    # Tier 4 : Description
    # --------------------------

    if query in description:
        return 0.40, "Description Match"

    return 0, "No Match"