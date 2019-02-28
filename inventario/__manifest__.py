# -*- coding: utf-8 -*-
{
    'name': "Inventario",

    'summary': "Gestión de las materias primas que entran y salen del inventario",

    'description': """
        El objetivo del módulo es  es que la persona encargada del inventario pueda gestionarlo de una forma más fácil, ya que podrá saber todo lo que tiene y así cuanto le queda y cuanto se va gastando.
    """,

    'author': "Jiann Pablo Zambrano",
    'website': "http://www.inventario_Restaurantes.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestión',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
