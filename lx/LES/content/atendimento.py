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
        name="inicio_sintomas",
        
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Início sintomas",
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name="retardo_diagnostico",
        
        searchable=True,
        widget=atapi.StringWidget(
            label="Retardo Diagnóstico",
        ),
    ),
    atapi.StringField(
        name="manifestacao_inicial",
        
        searchable=True,
        widget=atapi.StringWidget(
            label="Manisfestação Inicial",
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="cutaneo_agudo_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="cutaneo_subagudo_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="cutaneo_cronico_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="ulceras_orais_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="ulceras_nasais_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="alopecia_nao_cicatricial_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="articular_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="serosite_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="renal_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="neurologico_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="anemia_hemolitica_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="leucopenia_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="linfopenia_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="trombocitopenia_inf",
        searchable=True,
        schemata='Critérios Clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="fan_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="anti_dna_dupla_helice_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="anti_sm_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="antifosfolipidios_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="complemento_baixo_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="coombs_direto_inf",
        searchable=True,
        schemata='Critérios Imunológicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="miopatia_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="raynaud_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dano_hemorragia_alveolar_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="pnm_intersticial_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="vasculite_pele_sistemica_inf",
        searchable=True,
        schemata='Antecedentes clínicos',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Informações complementares"
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
            label="Início",
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name="tabaco_data_fim",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label="Término",
            show_hm=False,
        ),
    ),    
    atapi.TextField(
        name="tabaco_especificacao",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Especificação"
        ),
    ),
    atapi.StringField(
        name="tabaco_unidade_dia",       
        searchable=True,
        schemata='Comobidades',
        widget=atapi.StringWidget(
            label="Unidade/dia",
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
            label="Início",
            show_hm=False,
        ),
    ),
    atapi.DateTimeField(
        name="alcool_data_fim",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.CalendarWidget(
            label="Término",
            show_hm=False,  
        ),
    ),    
    atapi.TextField(
        name="alcool_especificacao",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Especificação"
        ),
    ),
    atapi.StringField(
        name="alcool_unidade_dia",
        searchable=True,
        schemata='Comobidades',
        widget=atapi.StringWidget(
            label="Unidade/dia",
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="has_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="diabete_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dislipidemia_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hipotireoidismo_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dac_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="ivp_varizes_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="asma_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dpoc_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="insuficiencia_cardiaca_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hipertensao_pulmonar_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="op_baixa_dmo_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="fm_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="depressao_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="sogren_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="saf_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="trombose_detalhes",
        searchable=True,
        schemata='Comobidades',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Detalhes adicionais"
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
            label="Detalhes adicionais"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="influenza_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="influenza_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="meningo_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="meningo_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="fa_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="fa_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="pneumo_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="pneumo_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="dtpa_dt_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="dtpa_dt_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hbv_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="hbv_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hav_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="hav_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hpv_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="hpv_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="hib_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="hib_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
        ),
    ),
    atapi.TextField(
        name="hib_anti_hbs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Anti-HBs"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="scr_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="scr_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="polio_vip_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="polio_vip_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Data",
            show_hm=False,
        ),
    ),
    atapi.TextField(
        name="varicela_obs",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Observações"
        ),
    ),
    atapi.TextField(
        name="varicela_dose",
        searchable=True,
        schemata='Vacinações',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label="Doses"
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
            label="Droga, dose e efeito"
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
            label="Especificar a indicação, início, dose número de sessões"
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
