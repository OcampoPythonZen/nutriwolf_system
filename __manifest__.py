# -*- coding: utf-8 -*-
{
    'name': "NUTRIWOLF",

    'summary': """
        Sistema de Nutricion
        """,

    'description': """
        Sistema de nutrición y control dedicado a dar una mejor
        calidad de vida a nuestros pacientes, haciendolos sentir
        plenos y ayudandolos a lograr sus objetivos alimentarios.
    """,

    'author': "Edgar y Luis Ocampo",
    'website': "https://nutriwolf.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/nutriwolf_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}