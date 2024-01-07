# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleInherit(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    state = fields.Selection(selection_add=[('qwe', 'quotation confirmed'), ('sale',)])

    ask_id = fields.Many2one('res.users')

    def confirm_test(self):
        for rec in self:
            rec.state = 'qwe'

    def confirm_test2(self):
        return {'type': 'ir.actions.act_window_close'}
        print("weew")
