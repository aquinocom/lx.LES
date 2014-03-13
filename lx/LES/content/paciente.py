# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.folder import ATFolder

# Product imports
from lx.LES.interfaces.contents import IPaciente
from lx.LES import LESMessageFactory as _
from lx.LES import config

# Schema definition
schema = ATFolder.schema.copy() + atapi.Schema((
    atapi.StringField(
        name="identificador_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Identificador",
            label_msgid=_(u"label_nome"),
        ),
    ),
    atapi.StringField(
        name="nome_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Nome",
            label_msgid=_(u"label_nome"),
        ),
    ),
    atapi.DateTimeField(
        name="nascimento_paciente",
        required=True,
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Data nascimento",
            label_msgid=_(u"label_nascimento"),
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name="idade_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Idade",
            label_msgid=_(u"label_idade"),
        ),
    ),
    atapi.StringField(
        name="uf_nasc_paciente",
        required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label="UF nasc",
            label_msgid=_(u"label_uf_nasc"),
        ),
        vocabulary=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
                    'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR',
                    'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    ),
    atapi.StringField(
        name="sexo_paciente",
        required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label="Sexo",
            label_msgid=_(u"label_uf_nasc"),
        ),
        vocabulary=["Masculino", "Feminino"]
    ),
    atapi.StringField(
        name="ocupacao_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Ocupação",
            label_msgid=_(u"label_ocupacao"),
        ),
    ),
    atapi.StringField(
        name="formacao_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Nível de formação",
            label_msgid=_(u"label_formação"),
        ),
    ),
    atapi.StringField(
        name="raca_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Raça",
            label_msgid=_(u"label_raca"),
        ),
    ),
    atapi.StringField(
        name="end_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Endereço",
            label_msgid=_(u"label_end"),
        ),
    ),
    atapi.StringField(
        name="bairro_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Bairro ou Satélite:",
            label_msgid=_(u"label_bairro"),
        ),
    ),
    atapi.StringField(
        name="cidade_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Cidade",
            label_msgid=_(u"label_cidade"),
        ),
    ),
    atapi.StringField(
        name="uf_paciente",
        required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label="UF",
            label_msgid=_(u"label_uf"),
        ),
        vocabulary=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
                    'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR',
                    'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    ),
    atapi.StringField(
        name="cep_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="CEP",
            label_msgid=_(u"label_cep"),
        ),
    ),
    atapi.StringField(
        name="fone_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Fone residencial",
            label_msgid=_(u"label_fone"),
        ),
    ),
    atapi.StringField(
        name="cel_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Celular",
            label_msgid=_(u"label_cel"),
        ),
    ),
    atapi.StringField(
        name="nome_parente_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Nome parente ou amigo",
            label_msgid=_(u"label_nome_parente"),
        ),
    ),
    atapi.StringField(
        name="fone_parente_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Fone parente ou amigo",
            label_msgid=_(u"label_fone_parente"),
        ),
    ),
),)

schemata.finalizeATCTSchema(schema)


class Paciente(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(IPaciente)

    meta_type = 'Paciente'
    portal_type = 'Paciente'

    _at_rename_after_creation = True

    schema = schema

atapi.registerType(Paciente, config.PROJECTNAME)
