NAME_KEY = "name"
ITEMS_KEY = "items"
PRICE_KEY = "price"

STORES = [
    {
        NAME_KEY: "My Wonderful Store",
        ITEMS_KEY: [
            {
                NAME_KEY: "My Item",
                PRICE_KEY: 15.99
            },
            {
                NAME_KEY: "My Item 2",
                PRICE_KEY: 19.99
            }
        ]
    }
]


def validate_item(item: dict) -> bool:
    """Validate an item"""
    return NAME_KEY in item and PRICE_KEY in item
