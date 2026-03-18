{
    'name': 'Material Loan',
    'version': '16.0.1.0.0',
    'summary': 'Control de prestamos de material del instituto',
    'author': 'Raul Hernandez y Juan Zornoza',
    'category': 'Tools',
    'license': 'LGPL-3',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/loan_views.xml',
        'views/dashboard_views.xml',
        'views/loan_report.xml',
    ],

    'installable': True,
    'application': True,
}
