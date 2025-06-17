# -*- coding: utf-8 -*-
# from odoo import http


# class TcuAmpliacion(http.Controller):
#     @http.route('/tcu_ampliacion/tcu_ampliacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tcu_ampliacion/tcu_ampliacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tcu_ampliacion.listing', {
#             'root': '/tcu_ampliacion/tcu_ampliacion',
#             'objects': http.request.env['tcu_ampliacion.tcu_ampliacion'].search([]),
#         })

#     @http.route('/tcu_ampliacion/tcu_ampliacion/objects/<model("tcu_ampliacion.tcu_ampliacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tcu_ampliacion.object', {
#             'object': obj
#         })

