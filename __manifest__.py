{
    'name': 'TCU Ampliación',
    'version': '1.0',
    'summary': 'Ampliación del módulo TCU para control académico y reportería',
    'author': 'Darvin Gutiérrez Altamirano',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/profesor_views.xml',
        'views/estudiante_views.xml',
        'views/observacion_views.xml',
        'views/historial_estado_views.xml',
        'views/reporte_estudiante_template.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

