# Variant Photo Manager by Amofordesign

This Odoo 17 module allows shop managers to easily manage images for product variants from the backend wizard interface.

## Features

- ✅ Upload a default image (`image_1920`) for all product variants that share:
  - The same product template
  - The same `Couleurs` attribute value

- ✅ Upload additional media images to each matching variant using `product.image`

- 🗑️ Delete all existing media images for matching variants with one click

## Use Cases

- Bulk-apply photos for all variants of a product with a specific color
- Quickly replace outdated images across multiple variants
- Clean up additional media for organized product displays

## How to Use

1. Go to **Website > eCommerce > Upload Variant Photo**
2. Select:
   - A base variant to derive the product template
   - A color attribute (`Couleurs`)
   - Upload an image file
3. Click:
   - **Upload and Apply**: sets main image
   - **Upload as Media**: adds additional image
   - **Delete Media**: removes all additional images for those variants

## Technical

- Compatible with Odoo 17.0
- Uses standard Odoo `product.image` and `image_1920` fields
- Requires `website_sale` and `product` modules

---

© 2024 Amofordesign — Released under the LGPL-3 license
# varian_media_upload