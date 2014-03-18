# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.Archetypes.utils import DisplayList
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.MasterSelectWidget.MasterSelectWidget import MasterSelectWidget

# Product imports
from lx.LES.interfaces.contents import IAtendimento
from lx.LES import LESMessageFactory as _
from lx.LES import config

# Schema definition
schema = ATCTContent.schema.copy() + atapi.Schema((
    atapi.DateTimeField(
        name="inicio_sintomas_atend",
        
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Início sintomas",
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name="retardo_atend",
        
        searchable=True,
        widget=atapi.StringWidget(
            label="Retardo Diagnóstico",
        ),
    ),
    atapi.StringField(
        name="manif_inicial_atend",
        
        searchable=True,
        widget=atapi.StringWidget(
            label="Manisfestação Inicial",
        ),
    ),
    
    #criterios classificatorios de LES
    #criterios clinicos
    atapi.StringField(
        name='criterio_clinico_1a',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        schemata='Critérios Clínicos',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1.a. Cutâneo agudo"),
            description=_(u"Erupção malar, bolhosa, maculo-papular ou\
            de fotossensibilidade OU psoriasiforme,\
            anular policíclica"),
            slave_fields=(dict(name='data_criterio_clinico_1a',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_1a',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_1a",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_1a",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_1b',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1.b. Cutâneo subagudo"),
            slave_fields=(dict(name='data_criterio_clinico_1b',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_1b',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_1b",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_1b",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_2',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"2. Cutâneo crônico"),
            description="Lúpus discoide, hipertrófico (verrucose),\
                        profundus (paniculite), túmidus, pérnio",
            slave_fields=(dict(name='data_criterio_clinico_2',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_2',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_2",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_2",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_3a',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3.a. Úlceras orais"),
            slave_fields=(dict(name='data_criterio_clinico_3a',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_3a',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_3a",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_3a",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_3b',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3.b. Úlceras nasais"),
            slave_fields=(dict(name='data_criterio_clinico_3b',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_3b',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_3b",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_3b",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_4',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"4. Alopecia não cicatricial"),
            description=_(u"Rarefação ou fragilidade capilar difusa"),
            slave_fields=(dict(name='data_criterio_clinico_4',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_4',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_4",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_4",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_5',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"5. Articular"),
            description=_(u"Sinovite (edema/derrame) OU\
                          artralgia com rigidez matinal>\
                          30 min, em ≥2 articulações"),
            slave_fields=(dict(name='data_criterio_clinico_5',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_5',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_5",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_5",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_6',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"6. Serosite"),
            description=_(u"Pleurisia, derrame ou atrito pleural OU\
                          dor, derrame OU atrito pericárdico OU\
                          pericardite ao ECG"),
            slave_fields=(dict(name='data_criterio_clinico_6',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_6',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_6",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_6",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_7',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"7. Renal"),
            description=_(u"Protenúria ≥ 500 mg  ou cilindros hemáticos"),
            slave_fields=(dict(name='data_criterio_clinico_7',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_7',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_7",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_7",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_8',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"8. Neurológico"),
            description=_(u"Convulsão, psicose, \
                          mononeurite, mielite, \
                          neuropatia periférica \
                          ou craniana, estado \
                          confusional agudo"),
            slave_fields=(dict(name='data_criterio_clinico_8',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_8',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_8",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_8",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_9',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"9. Anemia hemolitica"),
            slave_fields=(dict(name='data_criterio_clinico_9',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_9',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_9",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_9",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_10a',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"10.a. Leucopenia"),
            description=_(u"Leucopenia < 4000/mm3"),
            slave_fields=(dict(name='data_criterio_clinico_10a',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_10a',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_10a",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_10a",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_10b',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"10.b. Linfopenia"),
            description=_(u"Linfopenia < 1000/mm3"),
            slave_fields=(dict(name='data_criterio_clinico_10b',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_10b',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_10b",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_10b",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_11',
        searchable=True,
        schemata='Critérios Clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"11. Trombocitopenia"),
            description=_(u"< 100.000/mm3"),
            slave_fields=(dict(name='data_criterio_clinico_11',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_clinico_11',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_11",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_clinico_11",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    #criterios imunologicos
    atapi.StringField(
        name='criterio_imunologico_1',
        searchable=True,
        schemata='Critérios Imunológicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1. FAN"),
            description=_(u"> limite superior de referência"),
            slave_fields=(dict(name='data_criterio_imunologico_1',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_imunologico_1',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_imunologico_1",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_imunologico_1",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_imunologico_2',
        searchable=True,
        schemata='Critérios Imunológicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"2. Anti-DNA dupla hélice"),
            description=_(u"Reagente (>2x limite superior de referência, \
                          se ELISA)"),
            slave_fields=(dict(name='data_criterio_imunologico_2',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_imunologico_2',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_imunologico_2",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_imunologico_2",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_imunologico_2',
        searchable=True,
        schemata='Critérios Imunológicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"2. Anti-DNA dupla hélice"),
            description=_(u"Reagente (>2x limite superior de referência, \
                          se ELISA)"),
            slave_fields=(dict(name='data_criterio_imunologico_2',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_imunologico_2',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_imunologico_2",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_imunologico_2",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_imunologico_3',
        searchable=True,
        schemata='Critérios Imunológicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3. Anti SM"),
            description=_(u"Positivo"),
            slave_fields=(dict(name='data_criterio_imunologico_3',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_imunologico_3',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_imunologico_3",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_imunologico_3",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_imunologico_4',
        searchable=True,
        schemata='Critérios Imunológicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"4. Antifosfolipídios"),
            description=_(u"Anticoag. Iúpica, anti-cardiolip.\
                          (lgG, lgM, lgA, título médio), \
                          anti-β2-gp 1, VDRL ou RPR falso +"),
            slave_fields=(dict(name='data_criterio_imunologico_4',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_imunologico_4',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_imunologico_4",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_imunologico_4",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_imunologico_5',
        searchable=True,
        schemata='Critérios Imunológicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"5. Complemento baixo"),
            description=_(u"C3, C4 ou CH 50"),
            slave_fields=(dict(name='data_criterio_imunologico_5',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_imunologico_5',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_imunologico_5",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_imunologico_5",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='criterio_imunologico_6',
        searchable=True,
        schemata='Critérios Imunológicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"6. Coombs direto"),
            description=_(u"lndependente de emólise"),
            slave_fields=(dict(name='data_criterio_imunologico_6',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_criterio_imunologico_6',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_imunologico_6",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_criterio_imunologico_6",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),    
    #antecedentes clinicos
    atapi.StringField(
        name='antecedente_clinico_1',
        searchable=True,
        schemata='Antecedentes clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Miopatia"),
            slave_fields=(dict(name='data_antecedente_clinico_1',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_antecedente_clinico_1',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_antecedente_clinico_1",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_antecedente_clinico_1",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='antecedente_clinico_2',
        searchable=True,
        schemata='Antecedentes clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Raynaud"),
            slave_fields=(dict(name='data_antecedente_clinico_2',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_antecedente_clinico_2',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_antecedente_clinico_2",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_antecedente_clinico_2",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='antecedente_clinico_3',
        searchable=True,
        schemata='Antecedentes clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Dano/hemorragia alveolar"),
            slave_fields=(dict(name='data_antecedente_clinico_3',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_antecedente_clinico_3',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_antecedente_clinico_3",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_antecedente_clinico_3",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='antecedente_clinico_4',
        searchable=True,
        schemata='Antecedentes clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"PNM intersticial"),
            slave_fields=(dict(name='data_antecedente_clinico_4',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_antecedente_clinico_4',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_antecedente_clinico_4",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_antecedente_clinico_4",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    atapi.StringField(
        name='antecedente_clinico_5',
        searchable=True,
        schemata='Antecedentes clínicos',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Vasculite (pele/sistêmica)"),
            slave_fields=(dict(name='data_antecedente_clinico_5',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='inf_antecedente_clinico_5',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="data_antecedente_clinico_5",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="inf_antecedente_clinico_5",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
        ),
    ),
    #comobidades
    atapi.StringField(
        name='comobidade_1',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Tabaco"),
            slave_fields=(dict(name='data_inicio_comobidade_1',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='data_fim_comobidade_1',
                               action='show',
                               hide_values=('sim',)),                          
                          dict(name='especificacao_comobidade_1',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='unidade_comobidade_1',
                               action='show',
                               hide_values=('sim',)),)           
        ),
    ),
    atapi.DateTimeField(
        name="data_inicio_comobidade_1",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label="Início",
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name="data_fim_comobidade_1",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label="Término",
            show_hm=False,
        ),
    ),    
    atapi.TextField(
        name="especificacao_comobidade_1",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Especificação"
        ),
    ),
    atapi.StringField(
        name="unidade_comobidade_1",       
        searchable=True,
        schemata='Comobidades',
        widget=atapi.StringWidget(
            label="Unidade/dia",
        ),
    ),
    atapi.StringField(
        name='comobidade_2',
        searchable=True,
        schemata='Comobidades',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Álcool"),
            slave_fields=(dict(name='data_inicio_comobidade_2',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='data_fim_comobidade_2',
                               action='show',
                               hide_values=('sim',)),                          
                          dict(name='especificacao_comobidade_2',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='unidade_comobidade_2',
                               action='show',
                               hide_values=('sim',)),)           
        ),
    ),
    atapi.DateTimeField(
        name="data_inicio_comobidade_2",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label="Início",
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name="data_fim_comobidade_2",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label="Término",
            show_hm=False,  
        ),
    ),    
    atapi.TextField(
        name="especificacao_comobidade_2",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Especificação"
        ),
    ),
    atapi.StringField(
        name="unidade_comobidade_2",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.StringWidget(
            label="Unidade/dia",
        ),
    ),      
),)

schema['title'].widget.visible['edit'] = 'invisible'
schema['description'].widget.visible['edit'] = 'invisible'
schemata.finalizeATCTSchema(schema)


class Atendimento(ATCTContent):
    """
    """
    security = ClassSecurityInfo()
    implements(IAtendimento)

    meta_type = 'Atendimento'
    portal_type = 'Atendimento'

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        """
        """
        transaction.commit()
        normalizer = getUtility(IIDNormalizer)
        data_consulta = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        titulo = 'Atendimento:  ' + data_consulta
        new_id = normalizer.normalize(titulo)
        self.setTitle(titulo)
        self.setId(new_id)

    def getPacienteExame(self):
        """Retorna qual o paciente está vinculado ao exame
        """
        paciente = self.aq_parent
        return paciente.UID()

    schema = schema

atapi.registerType(Atendimento, config.PROJECTNAME)
