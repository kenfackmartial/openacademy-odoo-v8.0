# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """ Curso técnico de Odoo 8 """,

    'description': """
    """,

    'author': "Daniel Gómez Villegas",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','board'],

    # always loaded
    'data': [
    'security/security.xml',
    'security/ir.model.access.csv',
	'view/openacademy_course_view.xml',
	'view/openacademy_session_view.xml',
	'view/partner_view.xml',
    'view/openacademy_wizard_view.xml',
    'workflow/openacademy_session_workflow.xml',
    'report/openacademy_session_report.xml',
    'view/openacademy_session_board.xml',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
