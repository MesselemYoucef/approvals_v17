# -*- coding: utf-8 -*-
{
    'name': 'Approvals',
    'version': '1.0',
    'summary': 'Calculate the Credit Limit for the customers',
    'sequence': -102,
    'description': """Calculate the Credit Limit for the customers""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'base',
        'sale'
    ],
    'data': [
        'security/security.xml',
        'views/sale_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
