# -*- coding: utf-8 -*-
# from odoo import http


# class SaleInherit(http.Controller):
#     @http.route('/sale_inherit/sale_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_inherit/sale_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_inherit.listing', {
#             'root': '/sale_inherit/sale_inherit',
#             'objects': http.request.env['sale_inherit.sale_inherit'].search([]),
#         })

#     @http.route('/sale_inherit/sale_inherit/objects/<model("sale_inherit.sale_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_inherit.object', {
#             'object': obj
#         })
