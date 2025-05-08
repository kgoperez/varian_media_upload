{
    "name": "Variant Photo Manager by Amofordesign",
    "version": "17.0.1.0.0",
    "summary": "Manage default and additional images for product variants",
    "description": """
        This module allows uploading and managing both the main (default) and additional (media) images 
        for product variants based on color attributes.

        Features:
        - Upload a main image (`image_1920`) to all variants matching a selected color
        - Add an additional gallery image (`product.image`) to matching variants
        - Remove all additional images from matching variants
    """,
    "author": "Amofordesign",
    "website": "https://www.amofordesign.com",
    "license": "LGPL-3",
    "category": "Website/eCommerce",
    "depends": [
        "website_sale",
        "product"
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/variant_photo_wizard_view.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "currency": "EUR",
    "price": 49.99,
}
