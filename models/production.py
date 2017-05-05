from odoo import api, models, fields, _

class MrpProduction(models.Model):

    _inherit = 'mrp.production'

    @api.multi
    def button_add_raw(self):
        self.ensure_one()
        return {
            'name': _('Add Raw'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'stock.move',
            'view_id': self.env.ref('mrp_add_raw.mrp_add_raw_form_view').id,
            'type': 'ir.actions.act_window',
            'context': {
                'default_name': self.name,
                'default_date': self.date_planned_start,
                'default_location_id': self.location_src_id.id,
                'default_raw_material_production_id': self.id,
                'default_company_id': self.company_id.id,
                'default_operation_id': False,
                'default_procure_method': 'make_to_stock',
                'default_origin': self.name,
                'default_warehouse_id': self.location_src_id.get_warehouse().id,
                'default_group_id': self.procurement_group_id.id,
                'default_propagate': self.propagate,
                'onchange': 'mrp_add_raw',
                'mrp_production_id': self.id
            },
            'target': 'new',
        }
