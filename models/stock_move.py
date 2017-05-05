from odoo import api, models, fields, _

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def action_add_raw(self):
        self.action_confirm()
        return {'type': 'ir.actions.act_window_close'}

    @api.onchange('product_id', 'product_uom_qty', 'product_uom')
    def onchange_add_raw_form(self):
        onchange = self.env.context.get('onchange')
        mrp_production_id = self.env.context.get('mrp_production_id')
        if onchange and mrp_production_id and onchange == 'mrp_add_raw':
            mrp_production = self.env['mrp.production'].browse(mrp_production_id)
            if not mrp_production:
                return
            if not self.product_id:
                return

            original_quantity = mrp_production.product_qty - mrp_production.qty_produced
            self.location_dest_id = mrp_production.product_id.property_stock_production
            self.price_unit = self.product_id.standard_price
            self.unit_factor = self.product_uom_qty / original_quantity
