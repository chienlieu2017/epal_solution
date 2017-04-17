# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2009-2017 4Leaf Team
#
##############################################################################

{
    'name': "Web Epal Base",

    'summary': """
        Module for Epal.vn.""",

    'author': "Thuan LT",

    'website': "epal.vn",
    'category': 'web',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',

    'depends': [
        'base',
        'web',
        'website',
        'disable_odoo_online',
    ],
    'qweb': [
        'static/src/xml/web_dialog_size.xml',
        'view/base_view.xml',
    ],
    'data': [
        'view/qweb.xml',
        'view/web_template.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'active': True,
}
