# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/nutriwolf(http.Controller):
#     @http.route('/extra-addons/nutriwolf/extra-addons/nutriwolf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/nutriwolf/extra-addons/nutriwolf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/nutriwolf.listing', {
#             'root': '/extra-addons/nutriwolf/extra-addons/nutriwolf',
#             'objects': http.request.env['extra-addons/nutriwolf.extra-addons/nutriwolf'].search([]),
#         })

#     @http.route('/extra-addons/nutriwolf/extra-addons/nutriwolf/objects/<model("extra-addons/nutriwolf.extra-addons/nutriwolf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/nutriwolf.object', {
#             'object': obj
#         })