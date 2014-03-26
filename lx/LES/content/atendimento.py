# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements
from zope.component import getUtility
import transaction

# Security
from AccessControl import ClassSecurityInfo

#plone
from plone.i18n.normalizer.interfaces import IIDNormalizer

#Libs
from datetime import datetime

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.MasterSelectWidget.MasterSelectWidget import MasterSelectWidget

# Product imports
from lx.LES.interfaces.contents import IAtendimento
from lx.LES import LESMessageFactory as _
from lx.LES import config

# Schema definition
schema = ATCTContent.schema.copy() + atapi.Schema((
    atapi.DateTimeField(
        name="inicio_sintomas",
        searchable=True,
        widget=atapi.CalendarWidget(
            label=_(u"Início sintomas"),
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name="retardo_diagnostico",
        searchable=True,
        widget=atapi.StringWidget(
            label=_(u"Retardo Diagnóstico"),
        ),
    ),
    atapi.StringField(
        name="manifestacao_inicial",
        searchable=True,
        widget=atapi.StringWidget(
            label=_(u"Manisfestação Inicial"),
        ),
    ),

#criterios classificatorios de LES
#criterios clinicos
    atapi.StringField(
        name='cutaneo_agudo',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        schemata='Critérios Clínicos',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1.a. Cutâneo agudo"),
            description=_(u"Erupção malar, bolhosa, maculo-papular ou\
            de fotossensibilidade OU psoriasiforme,\
            anular policíclica"),
            slave_fields=(dict(name='cutaneo_agudo_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='cutaneo_agudo_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="cutaneo_agudo_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="cutaneo_agudo_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='cutaneo_subagudo',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1.b. Cutâneo subagudo"),
            slave_fields=(dict(name='cutaneo_subagudo_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='cutaneo_subagudo_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="cutaneo_subagudo_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="cutaneo_subagudo_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='cutaneo_cronico',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"2. Cutâneo crônico"),
            description="Lúpus discoide, hipertrófico (verrucose),\
                        profundus (paniculite), túmidus, pérnio",
            slave_fields=(dict(name='cutaneo_cronico_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='cutaneo_cronico_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="cutaneo_cronico_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="cutaneo_cronico_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='ulceras_orais',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3.a. Úlceras orais"),
            slave_fields=(dict(name='ulceras_orais_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='ulceras_orais_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="ulceras_orais_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="ulceras_orais_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='ulceras_nasais',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3.b. Úlceras nasais"),
            slave_fields=(dict(name='ulceras_nasais_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='ulceras_nasais_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="ulceras_nasais_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="ulceras_nasais_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='alopecia_nao_cicatricial',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"4. Alopecia não cicatricial"),
            description=_(u"Rarefação ou fragilidade capilar difusa"),
            slave_fields=(dict(name='alopecia_nao_cicatricial_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='alopecia_nao_cicatricial_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="alopecia_nao_cicatricial_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="alopecia_nao_cicatricial_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='articular',
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
            slave_fields=(dict(name='articular_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='articular_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="articular_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="articular_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='serosite',
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
            slave_fields=(dict(name='serosite_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='serosite_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="serosite_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="serosite_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='renal',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"7. Renal"),
            description=_(u"Protenúria ≥ 500 mg  ou cilindros hemáticos"),
            slave_fields=(dict(name='renal_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='renal_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="renal_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="renal_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='neurologico',
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
            slave_fields=(dict(name='neurologico_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='neurologico_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="neurologico_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="neurologico_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='anemia_hemolitica',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"9. Anemia hemolitica"),
            slave_fields=(dict(name='anemia_hemolitica_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='anemia_hemolitica_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="anemia_hemolitica_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="anemia_hemolitica_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='leucopenia',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"10.a. Leucopenia"),
            description=_(u"Leucopenia < 4000/mm3"),
            slave_fields=(dict(name='leucopenia_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='leucopenia_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="leucopenia_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="leucopenia_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='linfopenia',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"10.b. Linfopenia"),
            description=_(u"Linfopenia < 1000/mm3"),
            slave_fields=(dict(name='linfopenia_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='linfopenia_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="linfopenia_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="linfopenia_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='trombocitopenia',
        searchable=True,
        schemata='Critérios Clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"11. Trombocitopenia"),
            description=_(u"< 100.000/mm3"),
            slave_fields=(dict(name='trombocitopenia_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='trombocitopenia_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="trombocitopenia_data",
        searchable=True,
        schemata='Critérios Clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="trombocitopenia_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
#criterios imunologicos
    atapi.StringField(
        name='fan',
        searchable=True,
        schemata='Critérios Imunológicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1. FAN"),
            description=_(u"> limite superior de referência"),
            slave_fields=(dict(name='fan_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='fan_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="fan_data",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="fan_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='anti_dna_dupla_helice',
        searchable=True,
        schemata='Critérios Imunológicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"2. Anti-DNA dupla hélice"),
            description=_(u"Reagente (>2x limite superior de referência, \
                          se ELISA)"),
            slave_fields=(dict(name='anti_dna_dupla_helice_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='anti_dna_dupla_helice_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="anti_dna_dupla_helice_data",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="anti_dna_dupla_helice_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='anti_sm',
        searchable=True,
        schemata='Critérios Imunológicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3. Anti SM"),
            description=_(u"Positivo"),
            slave_fields=(dict(name='anti_sm_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='anti_sm_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="anti_sm_data",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="anti_sm_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='antifosfolipidios',
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
            slave_fields=(dict(name='antifosfolipidios_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='antifosfolipidios_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="antifosfolipidios_data",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="antifosfolipidios_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='complemento_baixo',
        searchable=True,
        schemata='Critérios Imunológicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"5. Complemento baixo"),
            description=_(u"C3, C4 ou CH 50"),
            slave_fields=(dict(name='complemento_baixo_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='complemento_baixo_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="complemento_baixo_data",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="complemento_baixo_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='coombs_direto',
        searchable=True,
        schemata='Critérios Imunológicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"6. Coombs direto"),
            description=_(u"lndependente de emólise"),
            slave_fields=(dict(name='coombs_direto_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='coombs_direto_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="coombs_direto_data",
        searchable=True,
        schemata='Critérios Imunológicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="coombs_direto_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
#antecedentes clinicos
    atapi.StringField(
        name='miopatia',
        searchable=True,
        schemata='Antecedentes clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Miopatia"),
            slave_fields=(dict(name='miopatia_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='miopatia_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="miopatia_data",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="miopatia_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='raynaud',
        searchable=True,
        schemata='Antecedentes clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Raynaud"),
            slave_fields=(dict(name='raynaud_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='raynaud_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="raynaud_data",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="raynaud_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='dano_hemorragia_alveolar',
        searchable=True,
        schemata='Antecedentes clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Dano/hemorragia alveolar"),
            slave_fields=(dict(name='dano_hemorragia_alveolar_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='dano_hemorragia_alveolar_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="dano_hemorragia_alveolar_data",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dano_hemorragia_alveolar_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='pnm_intersticial',
        searchable=True,
        schemata='Antecedentes clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"PNM intersticial"),
            slave_fields=(dict(name='pnm_intersticial_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pnm_intersticial_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="pnm_intersticial_data",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="pnm_intersticial_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
    atapi.StringField(
        name='vasculite_pele_sistemica',
        searchable=True,
        schemata='Antecedentes clínicos',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Vasculite (pele/sistêmica)"),
            slave_fields=(dict(name='vasculite_pele_sistemica_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='vasculite_pele_sistemica_inf',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="vasculite_pele_sistemica_data",
        searchable=True,
        schemata='Antecedentes clínicos',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="vasculite_pele_sistemica_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Informações complementares")
        ),
    ),
#comobidades
    atapi.StringField(
        name='tabaco',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Tabaco"),
            slave_fields=(dict(name='tabaco_data_inicio',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='tabaco_data_fim',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='tabaco_especificacao',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='tabaco_unidade_dia',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="tabaco_data_inicio",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Início"),
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name="tabaco_data_fim",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Término"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="tabaco_especificacao",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Especificação")
        ),
    ),
    atapi.StringField(
        name="tabaco_unidade_dia",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.StringWidget(
            label=_(u"Unidade/dia"),
        ),
    ),
    atapi.StringField(
        name='alcool',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Álcool"),
            slave_fields=(dict(name='alcool_data_inicio',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='alcool_data_fim',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='alcool_especificacao',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='alcool_unidade_dia',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="alcool_data_inicio",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Início"),
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name="alcool_data_fim",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Término"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="alcool_especificacao",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Especificação")
        ),
    ),
    atapi.StringField(
        name="alcool_unidade_dia",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.StringWidget(
            label=_(u"Unidade/dia"),
        ),
    ),
#outros
    atapi.StringField(
        name='has',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"HAS"),
            slave_fields=(dict(name='has_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='has_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="has_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="has_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='diabete',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Diabete"),
            slave_fields=(dict(name='diabete_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='diabete_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="diabete_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="diabete_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='dislipidemia',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Dislipidemia"),
            slave_fields=(dict(name='dislipidemia_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='dislipidemia_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="dislipidemia_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dislipidemia_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='hipotireoidismo',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Hipotireoidismo"),
            slave_fields=(dict(name='hipotireoidismo_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hipotireoidismo_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="hipotireoidismo_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hipotireoidismo_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='dac',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"DAC"),
            slave_fields=(dict(name='dac_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='dac_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="dac_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dac_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='ivp_varizes',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"IVP/Varizes"),
            slave_fields=(dict(name='ivp_varizes_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='ivp_varizes_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="ivp_varizes_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="ivp_varizes_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='asma',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Asma"),
            slave_fields=(dict(name='asma_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='asma_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="asma_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="asma_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='dpoc',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"DPOC"),
            slave_fields=(dict(name='dpoc_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='dpoc_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="dpoc_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dpoc_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='insuficiencia_cardiaca',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Insuficiência cardíaca"),
            slave_fields=(dict(name='insuficiencia_cardiaca_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='insuficiencia_cardiaca_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="insuficiencia_cardiaca_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="insuficiencia_cardiaca_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='hipertensao_pulmonar',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Hipertensão pulmonar"),
            slave_fields=(dict(name='hipertensao_pulmonar_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hipertensao_pulmonar_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="hipertensao_pulmonar_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hipertensao_pulmonar_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='op_baixa_dmo',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"OP/Baixa DMO"),
            slave_fields=(dict(name='op_baixa_dmo_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='op_baixa_dmo_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="op_baixa_dmo_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="op_baixa_dmo_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='fm',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"FM"),
            slave_fields=(dict(name='fm_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='fm_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="fm_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="fm_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='depressao',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Depressão"),
            slave_fields=(dict(name='depressao_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='depressao_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="depressao_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="depressao_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='sogren',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Sögren"),
            slave_fields=(dict(name='sogren_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='sogren_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="sogren_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="sogren_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='saf',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"SAF"),
            slave_fields=(dict(name='saf_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='saf_detalhes',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="saf_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="saf_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='trombose',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Trombose(s)"),
            slave_fields=(dict(name='trombose_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='trombose_detalhes',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='trombose_gestacional',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="trombose_data",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="trombose_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
    atapi.StringField(
        name='trombose_gestacional',
        searchable=True,
        schemata='Comobidades',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Gestacional?"),
            slave_fields=(dict(name='trombose_gestacional_detalhes',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.TextField(
        name="trombose_gestacional_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Detalhes adicionais")
        ),
    ),
#vacinacoes
    atapi.StringField(
        name='influenza',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Influenza"),
            slave_fields=(dict(name='influenza_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='influenza_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='influenza_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="influenza_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="influenza_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="influenza_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='meningo',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Meningo"),
            slave_fields=(dict(name='meningo_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='meningo_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='meningo_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="meningo_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="meningo_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="meningo_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='fa',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"FA"),
            slave_fields=(dict(name='fa_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='fa_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='fa_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="fa_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="fa_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="fa_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='pneumo',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Pneumo"),
            slave_fields=(dict(name='pneumo_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pneumo_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pneumo_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="pneumo_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="pneumo_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="pneumo_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='dtpa_dt',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"dTpa/dT"),
            slave_fields=(dict(name='dtpa_dt_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='dtpa_dt_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='dtpa_dt_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="dtpa_dt_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dtpa_dt_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="dtpa_dt_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='hbv',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"HBV"),
            slave_fields=(dict(name='hbv_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hbv_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hbv_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="hbv_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hbv_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="hbv_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='hav',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"HAV"),
            slave_fields=(dict(name='hav_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hav_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hav_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="hav_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hav_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="hav_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='hpv',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"HPV"),
            slave_fields=(dict(name='hpv_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hpv_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hpv_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="hpv_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hpv_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="hpv_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='hib',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"HIB"),
            slave_fields=(dict(name='hib_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hib_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hib_dose',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='hib_anti_hbs',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="hib_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hib_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="hib_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.TextField(
        name="hib_anti_hbs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Anti-HBs")
        ),
    ),
    atapi.StringField(
        name='scr',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"SCR"),
            slave_fields=(dict(name='scr_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='scr_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='scr_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="scr_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="scr_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="scr_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='polio_vip',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Pólio(VIP)"),
            slave_fields=(dict(name='polio_vip_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='polio_vip_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='polio_vip_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="polio_vip_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="polio_vip_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="polio_vip_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='varicela',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Varicela"),
            slave_fields=(dict(name='varicela_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='varicela_obs',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='varicela_dose',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.DateTimeField(
        name="varicela_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="varicela_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.TextField(
        name="varicela_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Doses")
        ),
    ),
    atapi.StringField(
        name='efeitos_adversos_medicamentosos',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Efeitos adversos medicamentosos"),
            slave_fields=(dict(name='efeitos_adversos_medicamentosos_obs',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.TextField(
        name="efeitos_adversos_medicamentosos_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Droga, dose e efeito")
        ),
    ),
    atapi.StringField(
        name='uso_ciclofosfamida',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Uso de ciclofosfamidas"),
            slave_fields=(dict(name='uso_ciclofosfamida_obs',
                               action='show',
                               hide_values=('sim',)),)
        ),
    ),
    atapi.TextField(
        name="uso_ciclofosfamida_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Especificar a indicação, início, dose número de sessões")
        ),
    ),
#continuacao
    atapi.StringField(
        name='corticosteroides',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Corticosteróides"),
            description=_(u"prednisona/deflazarcort/metilprednisolona/hidrocortisona"),
            slave_fields=(dict(name='corticosteroides_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='corticosteroides_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='corticosteroides_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='corticosteroides_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="corticosteroides_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="corticosteroides_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="corticosteroides_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.TextField(
        name="corticosteroides_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),

    atapi.StringField(
        name='pulsoterapia_ciclofosfamida',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Pulsoterapia com cilofosfamida"),
            description=_(u""),
            slave_fields=(dict(name='pulsoterapia_ciclofosfamida_num_pulsos_inducao',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pulsoterapia_ciclofosfamida_num_pulsos_manutencao',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pulsoterapia_ciclofosfamida_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pulsoterapia_ciclofosfamida_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pulsoterapia_ciclofosfamida_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pulsoterapia_ciclofosfamida_indicacao',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='pulsoterapia_ciclofosfamida_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="pulsoterapia_ciclofosfamida_num_pulsos_inducao",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"nº pulsos"),
            description=_(u"dose/indução"),
        ),
    ),
    atapi.DateTimeField(
        name="pulsoterapia_ciclofosfamida_num_pulsos_manutencao",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"nº pulsos"),
            description=_(u"dose/manutenção"),
        ),
    ),
    atapi.DateTimeField(
        name="pulsoterapia_ciclofosfamida_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="pulsoterapia_ciclofosfamida_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="pulsoterapia_ciclofosfamida_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.DateTimeField(
        name="pulsoterapia_ciclofosfamida_indicacao",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Indicação"),
        ),
    ),
    atapi.TextField(
        name="pulsoterapia_ciclofosfamida_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),
    atapi.StringField(
        name='metotretaxe',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Metotretaxe"),
            description=_(u""),
            slave_fields=(dict(name='metotretaxe_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='metotretaxe_dose_semanal',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='metotretaxe_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='metotretaxe_via',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='metotretaxe_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='metotretaxe_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="metotretaxe_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="metotretaxe_dose_semanal",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose semanal"),
        ),
    ),
    atapi.DateTimeField(
        name="metotretaxe_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="metotretaxe_via",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Via de administração"),
            description=_(u"(VO, IM, SC)"),
        ),
    ),
    atapi.DateTimeField(
        name="metotretaxe_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.TextField(
        name="metotretaxe_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),
    atapi.StringField(
        name='azatioprina',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Azatioprina"),
            description=_(u""),
            slave_fields=(dict(name='azatioprina_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='azatioprina_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='azatioprina_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='azatioprina_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="azatioprina_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="azatioprina_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="azatioprina_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.TextField(
        name="azatioprina_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),
    atapi.StringField(
        name='ciclosporina',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Ciclosporina"),
            description=_(u""),
            slave_fields=(dict(name='ciclosporina_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='ciclosporina_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='ciclosporina_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='ciclosporina_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="ciclosporina_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="ciclosporina_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="ciclosporina_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.TextField(
        name="ciclosporina_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),
    atapi.StringField(
        name='micofenolato_mofetil',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Micofenolato mofetil"),
            description=_(u""),
            slave_fields=(dict(name='micofenolato_mofetil_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='micofenolato_mofetil_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='micofenolato_mofetil_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='micofenolato_mofetil_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="micofenolato_mofetil_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="micofenolato_mofetil_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="micofenolato_mofetil_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.TextField(
        name="micofenolato_mofetil_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),
    atapi.StringField(
        name='cloroquina_hidroxicloroquina',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Cloroquina/hidroxicloroquina"),
            description=_(u""),
            slave_fields=(dict(name='cloroquina_hidroxicloroquina_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='cloroquina_hidroxicloroquina_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='cloroquina_hidroxicloroquina_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='cloroquina_hidroxicloroquina_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="cloroquina_hidroxicloroquina_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="cloroquina_hidroxicloroquina_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="cloroquina_hidroxicloroquina_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.TextField(
        name="cloroquina_hidroxicloroquina_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),
    atapi.StringField(
        name='outras_drogas',
        searchable=True,
        schemata='Vacinações',        
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Outras drogas"),
            description=_(u""),
            slave_fields=(dict(name='outras_drogas_dose_atual',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='outras_drogas_dose_total',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='outras_drogas_tempo',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='outras_drogas_efeitos',
                               action='show',
                               hide_values=('sim',)))           
        ),
    ),
    atapi.DateTimeField(
        name="outras_drogas_dose_atual",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose atual"),
        ),
    ),
    atapi.DateTimeField(
        name="outras_drogas_dose_total",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Dose total"),
        ),
    ),
    atapi.DateTimeField(
        name="outras_drogas_tempo",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.StringWidget(
            label=_(u"Tempo de uso"),
        ),
    ),
    atapi.TextField(
        name="outras_drogas_efeitos",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Efeitos colaterais")
        ),
    ),

    atapi.StringField(
        name='outros_medicamentos_atuais',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Medicamentos atuais para LES"),
            slave_fields=(dict(name='outros_medicamentos_atuais_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='outros_medicamentos_atuais_obs',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="outros_medicamentos_atuais_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="outros_medicamentos_atuais_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Especificar a droga, dose e efeito")
        ),
    ),
    atapi.StringField(
        name='anticoncepcional',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Anticoncepcional"),
            slave_fields=(dict(name='anticoncepcional_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='anticoncepcional_obs',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="anticoncepcional_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="anticoncepcional_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Queixas/ problemas atuais")
        ),
    ),
    atapi.StringField(
        name='ligadura',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Ligadura"),
            slave_fields=(dict(name='ligadura_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='ligadura_obs',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="ligadura_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="ligadura_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Queixas/ problemas atuais")
        ),
    ),
    atapi.StringField(
        name='histerectomia',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Histerectomia"),
            slave_fields=(dict(name='histerectomia_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='histerectomia_obs',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="histerectomia_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="histerectomia_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Queixas/ problemas atuais")
        ),
    ),
    atapi.StringField(
        name='menopausa',
        searchable=True,
        schemata='Vacinações',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"Menopausa"),
            slave_fields=(dict(name='menopausa_data',
                               action='show',
                               hide_values=('sim',)),
                          dict(name='menopausa_obs',
                               action='show',
                               hide_values=('sim',)))
        ),
    ),
    atapi.DateTimeField(
        name="menopausa_data",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.CalendarWidget(
            label=_(u"Data"),
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="menopausa_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Queixas/ problemas atuais")
        ),
    ),
#escalas analógicas
    atapi.IntegerField(
        name="fadiga",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.IntegerWidget(
            label=_(u"Fadiga")
        )
    ),
    atapi.IntegerField(
        name="qualidade_vida",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.IntegerWidget(
            label=_(u"Qualidade de vida")
        )
    ),
    atapi.IntegerField(
        name="saude_global",
        searchable=True,
        schemata='Vacinações',
        widget=atapi.IntegerWidget(
            label=_(u"Saúde global")
        )
    ),
#Avaliação de índices compostos
#SLICC / ACR, 2010
#dominio ocular
    atapi.StringField(
        name='slicc_acr_catarata',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1. Catarata"),
            description=_(u"Catarata em qualquer olho.\
                           Primária ou secundária à corticoterapia, \
                           documentada por oftalmoscopia."),
            slave_fields=(dict(name='catarata_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="catarata_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_alteracao_retinal',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"2. Alteração retinal"),
            description=_(u"Alteração retinal documentada por oftalmoscopia"),
            slave_fields=(dict(name='alteracao_retinal_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="alteracao_retinal_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_atrofia_optica',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3. Atrofia óptica"),
            description=_(u"Atrofia óptica documentada\
                           por exame oftalmoscópico"),
            slave_fields=(dict(name='atrofia_optica_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="atrofia_optica_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#dominio neuropisiquiátrico
    atapi.StringField(
        name='slicc_acr_disfuncao_cognitiva',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"4. Disfunção cognitiva"),
            description=_(u"Disfunção cognitiva (por exemplo,\
                           prejuízo de memória, dificuldade de cálculo,\
                           prejuízo da concentração, dificuldade\
                           de linguagem falada ou escrita) documentada\
                           por exame clínico ou teste neurocognitivo"),
            slave_fields=(dict(name='disfuncao_cognitiva_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="disfuncao_cognitiva_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_psicose',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"5. Psicose"),
            description=_(u"Psicose maior definida por distúrbios graves \
                           da percepção da realidade caracterizados\
                           por dellírios, atucinações auditivas ou visuais,\
                           incoerência, perda de associação de ideias,\
                           empobrecimento de ideias, \
                           pensamento ilógico, comportamento bizarro,\
                           desorganizado ou catatônico."),
            slave_fields=(dict(name='psicose_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="psicose_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_convulsoes',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"6. Convulsões"),
            description=_(u"Convulsões caracterizadas por movimentos \
                           tônicos e clônicos, requerendo terapia \
                           anticonvulsivante por mais de seis meses"),
            slave_fields=(dict(name='convulsoes_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="convulsoes_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_avc',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"7. AVC"),
            description=_(u"Acidente vascular cerebral que resulte em achados\
                           focais como paresia e fraqueza ou ressecção\
                           cirúrgica por outras causas, exceto malignidade"),
            slave_fields=(dict(name='avc_obs',
                               action='show',
                               hide_values=('1',)),
                          dict(name='slicc_acr_avc_mult_ocorrencia',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.StringField(
        name="slicc_acr_avc_mult_ocorrencia",
        searchable=True,
        schemata='Avaliação de índices',
        default='0',
        widget=atapi.SelectionWidget(
            label="Mais de 1(um) evento?",
            format="select"
        ),
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
    ),
    atapi.TextField(
        name="avc_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_neuropatia_craniana',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"8. Neuropatia craniana"),
            description=_(u"Neuropatia craniana ou periférica, excluindo-se\
                           neuropatia óptica, resultando em \
                           distúrbio motor ou sensitive"),
            slave_fields=(dict(name='neuropatia_craniana_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="neuropatia_craniana_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_mielite_transversa',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"9. Mielite transversa"),
            description=_(u"Mielite transversa (fraqueza de membros inferiores\
                           ou percla sensitiva com perda do central\
                           e esfincteriano retal e urinário)"),
            slave_fields=(dict(name='mielite_transversa_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="mielite_transversa_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#renal
    atapi.StringField(
        name='slicc_acr_tx_filtr_glomerular',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"10. Tx de filtr. Glomerular<50%"),
            slave_fields=(dict(name='tx_filtr_glomerular_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="tx_filtr_glomerular_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_proteinuria',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"11. Proteinúria ≥ 3,5 g/24 h"),
            slave_fields=(dict(name='proteinuria_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="proteinuria_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_insuficiencia_renal_terminal',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"12. Insuficiência renal terminal"),
            description=_(u"Insuficiência renal terminal"),
            slave_fields=(dict(name='insuficiencia_renal_terminal_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="insuficiencia_renal_terminal_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#pulmonar
    atapi.StringField(
        name='slicc_acr_hipertensao_pulmonar',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"13. Hipertensão pulmonar"),
            description=_(u"Hipertensão pulmonar (proeminência de ventrículo direito ou ausculta em foco pulmonar)."),
            slave_fields=(dict(name='hipertensao_pulmonar_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="hipertensao_pulmonar_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_fibrose_pulmonar',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"14. Fibrose pulmonar"),
            description=_(u"Fibrose pulmonar (exame físico e radiografia)."),
            slave_fields=(dict(name='fibrose_pulmonar_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="fibrose_pulmonar_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
        atapi.StringField(
        name='slicc_acr_shrinking_lung_syndrome',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"15. Shrinking lung syndrome"),
            description=_(u"Shrinking lung syndrome (radiografia)."),
            slave_fields=(dict(name='shrinking_lung_syndrome_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="shrinking_lung_syndrome_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_fibrose_pleural',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"16. Fibrose pleural"),
            description=_(u"Fibrose pleural (radiografia)."),
            slave_fields=(dict(name='fibrose_pleural_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="fibrose_pleural_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_infarto_pulmonar',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"17. Infarto pulmonar"),
            description=_(u"Infarto pulmonar (radiografia),\
                          ressecção por outra causa que não malignidade."),
            slave_fields=(dict(name='infarto_pulmonar_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="infarto_pulmonar_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#cardiovascular
    atapi.StringField(
        name='slicc_acr_angina_pectoris_angioplastia',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"18. Angina pectoris/angioplastia"),
            slave_fields=(dict(name='angina_pectoris_angioplastia_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="angina_pectoris_angioplastia_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_infarto_agudo_miocardio',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"19. Infarto agudo do miocárdio"),
            description=_(u"Infarto agudo do miocárdio documentado por\
                          eletrocardiograrna e perfil enzimático"),
            slave_fields=(dict(name='infarto_agudo_miocardio_obs',
                               action='show',
                               hide_values=('1',)),
                          dict(name='slicc_acr_infarto_agudo_miocardio_mult_ocorrencia',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.StringField(
        name="slicc_acr_infarto_agudo_miocardio_mult_ocorrencia",
        searchable=True,
        schemata='Avaliação de índices',
        default='0',
        widget=atapi.SelectionWidget(
            label="Mais de 1(um) evento?",
            format="select"
        ),
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
    ),
    atapi.TextField(
        name="infarto_agudo_miocardio_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_miocardiopatia',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"20. Miocardiopatia"),
            description=_(u"Mioocardiopatia\
                          (disfunção ventricular documentada clinicamente)."),
            slave_fields=(dict(name='miocardiopatia_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="miocardiopatia_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_doenca_valvular',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"21. Doença valvular"),
            description=_("Doença valvular (murmúrio diastólico\
                          ou sistólico > 3/6)."),
            slave_fields=(dict(name='doenca_valvular_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="doenca_valvular_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_doenca_valvular',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"22. Pericardite"),
            description=_("Pericardite por seis meses ou pericardiectomia."),
            slave_fields=(dict(name='doenca_valvular_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="doenca_valvular_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#vascular periferica
    atapi.StringField(
        name='slicc_acr_claudicacao_persistente',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"23. Claudicação persistente"),
            description=_(u"Perda tecidual menor (perda de polpa tecidual)."),
            slave_fields=(dict(name='claudicacao_persistente_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="claudicacao_persistente_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_claudicacao_persistente',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"24. Perda tecidual menor"),
            description=_(u"Perda tecidual menor (perda de polpa tecidual)."),
            slave_fields=(dict(name='claudicacao_persistente_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="claudicacao_persistente_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_perda_tecidual_menor',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"24. Perda tecidual menor"),
            description=_(u"Perda tecidual menor (perda de polpa tecidual)."),
            slave_fields=(dict(name='perda_tecidual_menor_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="perda_tecidual_menor_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_perda_tecidual_significante',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"25. Perda tecidual significante"),
            description=_(u"Perda tecidual significante (por exemplo, perda digital ou de membra)"),
            slave_fields=(dict(name='perda_tecidual_significante_obs',
                               action='show',
                               hide_values=('1',)),
                          dict(name='slicc_acr_perda_tecidual_significante_mult_ocorrencia',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.StringField(
        name="slicc_acr_perda_tecidual_significante_mult_ocorrencia",
        searchable=True,
        schemata='Avaliação de índices',
        default='0',
        widget=atapi.SelectionWidget(
            label="Mais de 1(um) evento?",
            format="select"
        ),
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
    ),
    atapi.TextField(
        name="perda_tecidual_significante_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_trombose_venosa_edema',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"26. Trombose venosa c/ edema"),
            description=_(u"Trombose venosa com edema, ulceração\
                          ou evidencia clínica de estase venosa."),
            slave_fields=(dict(name='trombose_venosa_edema_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="trombose_venosa_edema_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_infarto_resseccao_intest',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"27. Infarto ou ressecção intest."),
            description=_(u"Infarto ou ressenção intestinal abaixo do duodeno,\
                          baço, fígado ou vesícula biliar por qualquer causa."),
            slave_fields=(dict(name='infarto_resseccao_intest_obs',
                               action='show',
                               hide_values=('1',)),
                          dict(name='slicc_acr_infarto_resseccao_intest_mult_ocorrencia',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
#gastrointestinal
    atapi.StringField(
        name="slicc_acr_infarto_resseccao_intest_mult_ocorrencia",
        searchable=True,
        schemata='Avaliação de índices',
        default='0',
        widget=atapi.SelectionWidget(
            label="Mais de 1(um) evento?",
            format="select"
        ),
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
    ),
    atapi.TextField(
        name="infarto_resseccao_intest_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_insuficiencia_mesenterica',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"28. Insuficiência mesentérica"),
            description=_(u"Insuficiência mesentérica com dor abdominal difusa ao exame clínico."),
            slave_fields=(dict(name='insuficiencia_mesenterica_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="insuficiencia_mesenterica_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_peritonite_cronica_dor',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"29. Peritonite crônica c/ dor"),
            description=_(u"Peritonite crônica com dor abdominal \
                          persistente e irritação peritoneal."),
            slave_fields=(dict(name='peritonite_cronica_dor_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="peritonite_cronica_dor_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_constricao_esofagica_observ',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"30. Constrição esofágica observ."),
            description=_(u"Constrição esofágica observada por endoscopia\
                          ou cirurgia de trato gastrointestinal superior\
                          como correção da constrição, cirurgia\
                          cle úlcera. etc.. ou por história de \
                          insuficiência pancreática requerendo \
                          reposição enzimática ou por pseudocisto."),
            slave_fields=(dict(name='constricao_esofagica_observ_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="constricao_esofagica_observ_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#musculoessqueletica
    atapi.StringField(
        name='slicc_acr_atrofia_musc_fraqueza',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"31. Atrofia musc. ou fraqueza"),
            description=_(u"Atrofia muscular ou fraqueza muscular, \
                          demonstradas pelo exame físico."),
            slave_fields=(dict(name='atrofia_musc_fraqueza_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="atrofia_musc_fraqueza_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_artrite_deformante',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"32. Artrite deformante"),
            description=_(u"Artrite deformante ou erosiva \
                          (incluindo-se deformidades redutlíveis e\
                          excluindo-se osteonecrose) no exame fisico."),
            slave_fields=(dict(name='artrite_deformante_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="artrite_deformante_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_osteoporose_fratura',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"33. Osteoporose c/ fratura"),
            description=_(u"Osteoporose com fratura ou colapso vertebral\
                          (excluindo-se osteonecrose),a \
                          demonstrada radiograficamente."),
            slave_fields=(dict(name='osteoporose_fratura_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="osteoporose_fratura_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_osteonecrose_demonstrada',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"34. Osteonecrose demonstrada"),
            description=_(u"Osteonecrose demonstrada por \
                          qualquer técnica de imagem."),
            slave_fields=(dict(name='osteonecrose_demonstrada_obs',
                               action='show',
                               hide_values=('1',)),
                          dict(name='slicc_acr_osteonecrose_demonstrada_mult_ocorrencia',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.StringField(
        name="slicc_acr_osteonecrose_demonstrada_mult_ocorrencia",
        searchable=True,
        schemata='Avaliação de índices',
        default='0',
        widget=atapi.SelectionWidget(
            label="Mais de 1(um) evento?",
            format="select"
        ),
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
    ),
    atapi.TextField(
        name="osteonecrose_demonstrada_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_osteomielite_documentada',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"35. Osteomielite documentada"),
            description=_(u"Osteomielite documentada clinicamente\
                          e confirmada por cultura ou ruptura tendiníea."),
            slave_fields=(dict(name='osteomielite_documentada_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="osteomielite_documentada_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#dermatologico
    atapi.StringField(
        name='slicc_acr_alopecia_cicatricial_cronica',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"36. Alopécia cicatricial crônica"),
            description=_(u"Alopécia cicatricial crônica documentada clinicamente."),
            slave_fields=(dict(name='alopecia_cicatricial_cronica_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="alopecia_cicatricial_cronica_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_cicatriz_extensa_paniculite',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"37. Cicatriz extensa / paniculite"),
            description=_(u"Cicatriz extensa ou paniculite em localização \
                          diferente do couro cabeludo ou polpa tecidual, \
                          documentada clinicamente."),
            slave_fields=(dict(name='cicatriz_extensa_paniculite_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="cicatriz_extensa_paniculite_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='slicc_acr_ulceracao_cutanea',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"38. Ulceração cutânea"),
            description=_(u"Ulceração cutanea (excluindo-se trombose) por mais de seis meses."),
            slave_fields=(dict(name='ulceracao_cutanea_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="ulceracao_cutanea_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#falencia gono
    atapi.StringField(
        name='slicc_acr_amnorreia',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"39. Amnorreia"),
            description=_(u"Amenorreia secundária antes dos 40 anos de idade."),
            slave_fields=(dict(name='amnorreia_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="amnorreia_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#diabetes
    atapi.StringField(
        name='slicc_acr_diabetes_requerendo_tratam',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"40.Diabetes requerendo tratam."),
            description=_(u"Requerendo tratamento e independente deste."),
            slave_fields=(dict(name='diabetes_requerendo_tratam_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="diabetes_requerendo_tratam_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#malignidade
    atapi.StringField(
        name='slicc_acr_malignidade_documentada',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='0',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"41. Malignidade documentada"),
            description=_(u"Documentada por exame patológico, excluindo displasia"),
            slave_fields=(dict(name='malignidade_documentada_obs',
                               action='show',
                               hide_values=('1',)),
                          dict(name='slicc_acr_malignidade_documentada_mult_ocorrencia',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.StringField(
        name="slicc_acr_malignidade_documentada_mult_ocorrencia",
        searchable=True,
        schemata='Avaliação de índices',
        default='0',
        widget=atapi.SelectionWidget(
            label="Mais de 1(um) evento?",
            format="select"
        ),
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
    ),
    atapi.TextField(
        name="malignidade_documentada_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
#SLEDAI - 2K
    atapi.StringField(
        name='sledai_convulsao',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"1. Convulsão"),
            description=_(u"Início recente, excluídas causas metabólicas \
                          infecciosas e secundárias ao uso de drogas"),
            slave_fields=(dict(name='convulsao_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="convulsao_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_psicose',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"2. Psicose"),
            description=_(u"Distúrbio severo da percepcção da realidade, \
                          excluídas causas metabólicas e drogas. lnclui \
                          alucinações, incoerência, perda marcada das \
                          associações de ideias, pensamento pobre, ilógico; \
                          comportamento bizarro, desorganizado ou catatônico."),
            slave_fields=(dict(name='psicose_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="psicose_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_delirium',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"3. Delírium"),
            description=_(u"Alteração abrupta e flutuante das funções mentais,\
                          atingindo a orientação, a atenção, a memória e\
                          outras funções intelectuais. lnclui a redução da\
                          vigília, com diminuição da atenção, acompanhada de\
                          pelo menos dois sintomas descritos a seguir:\
                          perturbação da percepção, discurso incoerente, \
                          insônia ou hipersonia diurna, aumento ou redução \
                          da atividade psicomotora. Exclui causas metabólicas,\
                          infecciosas ou secundárias ao uso de drogas."),
            slave_fields=(dict(name='delirium_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="delirium_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_disturbios_visuais',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"4. Distúrbios visuais"),
            description=_(u"Alteração da retina caracterizada por corpos\
                          cistoides, hemorragias retinianas, exsudatos \
                          serosos ou hemorragias do plexo coroide ou\
                          neurite séptica. Excluir HTA, infecções e drogas."),
            slave_fields=(dict(name='disturbios_visuais_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="disturbios_visuais_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_comp_pares',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"5. Comp. dos pares"),
            description=_(u"Neuropatia sensorial ou motora, \
                          de inicio ou reinício recente."),
            slave_fields=(dict(name='comp_pares_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="comp_pares_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_cefaleia_lupica',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"6. Cefaleia lúpica"),
            description=_(u"Severa e persistente, do tipo enxaqueca que\
                          não responde a analgésicos convencionais."),
            slave_fields=(dict(name='cefaleia_lupica_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="cefaleia_lupica_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_acidente_vasc',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"7. Acidente vasc. Enc"),
            description=_(u"NPresença de AVE. Excluir causa aterosclerótica"),
            slave_fields=(dict(name='acidente_vasc_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="acidente_vasc_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_vasculite',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('8', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"8. Vasculite"),
            description=_(u"Ulcerações, gangrenas, infartos periungueais,\
                          nódulos digitais dolorosos, áreas hemorrágicas\
                          subungueais, biópsia ou angiografia de qualquer\
                          área do corpo apresentando vasculite"),
            slave_fields=(dict(name='vasculite_obs',
                               action='show',
                               hide_values=('8',)),)
        ),
    ),
    atapi.TextField(
        name="vasculite_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
        atapi.StringField(
        name='sledai_artrites',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('4', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"9. Artrites"),
            description=_(u"Ulcerações, gangrenas, infartos periungueais,\
                          nódulos digitais dolorosos, áreas hemorrágicas\
                          subungueais, biópsia ou angiografia de qualquer\
                          área do corpo apresentando artrites"),
            slave_fields=(dict(name='artrites_obs',
                               action='show',
                               hide_values=('4',)),)
        ),
    ),
    atapi.TextField(
        name="artrites_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_miosites',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('4', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"10. Miosites"),
            description=_(u"Dor ou fraqueza muscular proximal \
                          acompanhada de aumento de CPK / aldolase, \
                          eletromiografia alterada, biópsia\
                          compatível com miosite."),
            slave_fields=(dict(name='miosites_obs',
                               action='show',
                               hide_values=('4',)),)
        ),
    ),
    atapi.TextField(
        name="miosites_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
        atapi.StringField(
        name='sledai_cilindros_urinar',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('4', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"11. Cilindros urinár"),
            description=_(u"Hematicos, granuloses ou eritrocitarios"),
            slave_fields=(dict(name='cilindros_urinar_obs',
                               action='show',
                               hide_values=('4',)),)
        ),
    ),
    atapi.TextField(
        name="cilindros_urinar_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
        atapi.StringField(
        name='sledai_hematuria',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('4', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"12. Hematúria"),
            description=_(u"Mais de 5 eritrócitos/campo. Excluir outras \
                          causas tais como llitíase renal, infecções."),
            slave_fields=(dict(name='hematuria_obs',
                               action='show',
                               hide_values=('4',)),)
        ),
    ),
    atapi.TextField(
        name="hematuria_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
        atapi.StringField(
        name='sledai_proteinuria',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('4', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"13. Proteinúria"),
            description=_(u"Concentracção > a 0,5 g/24 horas"),
            slave_fields=(dict(name='proteinuria_obs',
                               action='show',
                               hide_values=('4',)),)
        ),
    ),
    atapi.TextField(
        name="proteinuria_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_piuria',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('4', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"14. Piúria"),
            description=_(u"Mais de 5 leucócitos/campo na \
                          ausência de infeccção"),
            slave_fields=(dict(name='piuria_obs',
                               action='show',
                               hide_values=('4',)),)
        ),
    ),
    atapi.TextField(
        name="piuria_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_rash_cutaneo',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('2', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"15. Rash cutâneo"),
            description=_(u"Mais de 5 leucócitos/campo na ausência de infeccção"),
            slave_fields=(dict(name='rash_cutaneo_obs',
                               action='show',
                               hide_values=('2',)),)
        ),
    ),
    atapi.TextField(
        name="rash_cutaneo_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
        atapi.StringField(
        name='sledai_alopecia',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('2', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"16. Alopécia"),
            description=_(u"início recente ou recorrente, excessiva, \
                          difusa ou localizada"),
            slave_fields=(dict(name='alopecia_obs',
                               action='show',
                               hide_values=('2',)),)
        ),
    ),
    atapi.TextField(
        name="alopecia_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_ulcera_mucosa',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('2', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"17. Úlcera de mucosa"),
            description=_(u"lnicio recente ou recorrente, nasais ou orais"),
            slave_fields=(dict(name='ulcera_mucosa_obs',
                               action='show',
                               hide_values=('2',)),)
        ),
    ),
    atapi.TextField(
        name="ulcera_mucosa_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_pleurisia',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('2', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"18. Pleurisia"),
            description=_(u"Dor pleurítica com atrito, derrame ou espessamento pleural"),
            slave_fields=(dict(name='pleurisia_obs',
                               action='show',
                               hide_values=('2',)),)
        ),
    ),
    atapi.TextField(
        name="pleurisia_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_pericardite',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('2', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"19. Pericardite"),
            description=_(u"Dor no peito, com atrito ou derrame pericardico,\
                          confirmado por EGG ou Ecocardiograma"),
            slave_fields=(dict(name='pericardite_obs',
                               action='show',
                               hide_values=('2',)),)
        ),
    ),
    atapi.TextField(
        name="pericardite_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_complemento_bai',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('2', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"20. Complemento bai"),
            description=_(u"CH50; C3 ou C4 abaixo dos valores de referência"),
            slave_fields=(dict(name='complemento_bai_obs',
                               action='show',
                               hide_values=('2',)),)
        ),
    ),
    atapi.TextField(
        name="complemento_bai_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_anti_dnads',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('2', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"21. Anti-DNAds"),
            description=_(u"Acima dos valores de referência do laboratório"),
            slave_fields=(dict(name='anti_dnads_obs',
                               action='show',
                               hide_values=('2',)),)
        ),
    ),
    atapi.TextField(
        name="anti_dnads_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_febre',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"22. Febre"),
            description=_(u"Temperatura axilar >38°, na ausência de processo infeccioso"),
            slave_fields=(dict(name='febre_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="febre_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_trombocitopenia',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"23. Trombocitopenia"),
            description=_(u"Concentração de plaquetas inferior a 100 000/mm3\
                          (excluídas causas farmacológicas)"),
            slave_fields=(dict(name='trombocitopenia_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="trombocitopenia_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),
    atapi.StringField(
        name='sledai_leucopenia',
        searchable=True,
        schemata='Avaliação de índices',
        vocabulary=[('0', 'Não'), ('1', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            #format='radio',
            label=_(u"24. Leucopenia"),
            description=_(u"Concentração de leucócitos inferior a 3 00/mm3, excluiías causas farmacológicas"),
            slave_fields=(dict(name='leucopenia_obs',
                               action='show',
                               hide_values=('1',)),)
        ),
    ),
    atapi.TextField(
        name="leucopenia_obs",
        searchable=True,
        schemata='Avaliação de índices',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label=_(u"Observações")
        ),
    ),    
),)

schema['title'].widget.visible['edit'] = 'invisible'
schema['description'].widget.visible['edit'] = 'invisible'
schemata.finalizeATCTSchema(schema)


class Atendimento(ATCTContent, HistoryAwareMixin):
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

    schema = schema

atapi.registerType(Atendimento, config.PROJECTNAME)
