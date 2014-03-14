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
        required=True,
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Início sintomas",
            label_msgid=_(u"label_inicio_sintomas_atend"),
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name="retardo_atend",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Retardo Diagnóstico",
            label_msgid=_(u"label_retardo_atend"),
        ),
    ),
    atapi.StringField(
        name="manif_inicial_atend",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Manisfestação Inicial",
            label_msgid=_(u"label_manif_inicial_atend"),
        ),
    ),
    atapi.StringField(
        name='criterio_clinico_1a',
        vocabulary=[('nao', 'Não'), ('sim', 'Sim')],
        default='nao',
        widget=MasterSelectWidget(
            label=_(u"1.a. Cutâneo agudo"),
            description=_(u"Erupção malar, bolhosa, maculo-papular ou\
            de fotossensibilidade OU psoriasiforme,\
            anular policíclica"),
            slave_fields=(dict(name='data_criterio_clinico_1a', action='show', hide_values=('sim',)),),
        ),
    ),
    atapi.DateTimeField(
        name="data_criterio_clinico_1a",
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Data",
            label_msgid=_(u"label_inicio_sintomas_atend"),
            show_hm=False,
        ),
    ),

),)

schemata.finalizeATCTSchema(schema)


class Atendimento(ATCTContent):
    """
    """
    security = ClassSecurityInfo()
    implements(IAtendimento)

    meta_type = 'Atendimento'
    portal_type = 'Atendimento'

    _at_rename_after_creation = True

    schema = schema

atapi.registerType(Atendimento, config.PROJECTNAME)
