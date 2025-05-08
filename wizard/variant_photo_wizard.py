from odoo import models, fields
import base64
import requests
from io import BytesIO
from odoo.exceptions import ValidationError, UserError


class VariantPhotoWizard(models.TransientModel):
    _name = 'variant.photo.wizard'
    _description = 'Upload Photos for product'

    upload_file = fields.Binary('Upload File', required=True)
    variant_id = fields.Many2one('product.product', string='Variant')
    attribute_value_id = fields.Many2one('product.attribute.value', string='Attribute Value',
                                         domain="[('attribute_id.name', '=', 'Couleurs')]")

    def action_upload_default(self):
        self.ensure_one()

        # Decode the uploaded image
        file_content = base64.b64decode(self.upload_file)
        if not file_content:
            raise UserError("The uploaded file is empty or invalid.")

        # Get the target template
        product_template = self.variant_id.product_tmpl_id

        # Find all variants of this template with the selected attribute value
        variants = self.env['product.product'].search([
            ('product_tmpl_id', '=', product_template.id),
            ('product_template_attribute_value_ids.product_attribute_value_id', '=', self.attribute_value_id.id)
        ])

        for variant in variants:
            variant.image_1920 = base64.b64encode(file_content)

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Success",
                'message': f"{len(variants)} variants updated with the new image.",
                'type': 'success',
                'sticky': False,
            }
        }

    def action_upload_media(self):
        self.ensure_one()

        # Decode the uploaded image
        file_content = base64.b64decode(self.upload_file)
        if not file_content:
            raise UserError("The uploaded file is empty or invalid.")

        # Get the target template
        product_template = self.variant_id.product_tmpl_id

        # Find all matching variants with this attribute value
        variants = self.env['product.product'].search([
            ('product_tmpl_id', '=', product_template.id),
            ('product_template_attribute_value_ids.product_attribute_value_id', '=', self.attribute_value_id.id)
        ])

        # Add image as a gallery image to each variant
        for variant in variants:
            self.env['product.image'].create({
                'image_256': base64.b64encode(file_content),
                'image_512': base64.b64encode(file_content),
                'image_1024': base64.b64encode(file_content),
                'image_1920': base64.b64encode(file_content),
                'product_variant_id': variant.id,
                'name': f"Media - {variant.display_name}",
            })

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Success",
                'message': f"{len(variants)} media images uploaded.",
                'type': 'success',
                'sticky': False,
            }
        }

    def action_delete_all_media(self):
        self.ensure_one()

        # Get the target template
        product_template = self.variant_id.product_tmpl_id

        # Find all matching variants with the selected attribute value
        variants = self.env['product.product'].search([
            ('product_tmpl_id', '=', product_template.id),
            ('product_template_attribute_value_ids.product_attribute_value_id', '=', self.attribute_value_id.id)
        ])

        # Find all gallery images (product.image) linked to these variants
        images = self.env['product.image'].search([
            ('product_variant_id', 'in', variants.ids)
        ])

        count = len(images)
        images.unlink()

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Media Deleted",
                'message': f"{count} media images removed from variants.",
                'type': 'warning',
                'sticky': False,
            }
        }
