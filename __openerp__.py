# -*- coding: utf-8 -*-
{
    'name' : 'OpenAcademy odoo v9',
    'version' : '1.0',
    'author' : 'Saber',
    'license': 'LGPL',
    'category' : 'Formation',
    'description' : """ Formation Odoo v9""",
    'website': '',
    'images' : [],
    'depends': ['base', 'board'],

                
    'data': [
            'views/openacademy.xml',
            'views/partner.xml',
            'views/session_workflow.xml',
            'security/security.xml',
            'security/ir.model.access.csv',
            'reports.xml',
            'views/session_board.xml',


             ],
             
    'qweb' : [],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}