# -*- coding: utf-8 -*-
"""Common configuration constants
"""

PROJECTNAME = 'lx.LES'

ADD_PERMISSIONS = {
    'AtendimentoMedicina': 'lx.LES: Add AtendimentoMedicina',
    'ExameUrina': 'lx.LES: Add ExameUrina',
    'ExameSangue': 'lx.LES: Add ExameSangue',
    'Paciente': 'lx.LES: Add Paciente',
}

PRODUCTS = [('Products.MasterSelectWidget', 0, 0, 1, 'Products.MasterSelectWidget:default', 1),
            ('aoki.kwidgets', 0, 0, 1, 'aoki.kwidgets:default', 1), ]
