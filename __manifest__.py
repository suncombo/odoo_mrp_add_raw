# -*- coding: utf-8 -*-
{
    'name': "Mrp Add Raw",

    'summary': "",

    'description': "",

    'author': "Mick",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mrp'],

    # always loaded
    'data': ['views/product_produce_views.xml'],
    # only loaded in demonstration mode
    'demo': [],
}