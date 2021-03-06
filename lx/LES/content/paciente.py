# -*- coding: utf-8 -*-

import datetime
from DateTime import DateTime
# Zope3 imports
from zope.interface import implements
from zope.component import getUtility
import transaction

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin

#plone
from plone.i18n.normalizer.interfaces import IIDNormalizer

# Product imports
from lx.LES.interfaces.contents import IPaciente
from lx.LES import LESMessageFactory as _
from lx.LES import config

# Schema definition
schema = ATFolder.schema.copy() + atapi.Schema((
    atapi.StringField(
        name="title",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Nome",
            label_msgid=_(u"label_nome"),
        ),
    ),

    atapi.StringField(
        name="prontuario_paciente",
        required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label="Prontuário",
            label_msgid=_(u"label_prontuario"),
        ),
    ),

    atapi.StringField(
        name="identificador_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Identificador",
            label_msgid=_(u"label_identificador"),
            helper_js=('++resource++paciente.js', '++resource++jquery.maskedinput.js'),
        ),
    ),


    #atapi.StringField(
    #    name="rg_paciente",
    #    searchable=True,
    #    widget=atapi.StringWidget(
    #        label="RG",
    #        label_msgid=_(u"label_rg"),
    #    ),
    #),

    atapi.StringField(
        name="cpf_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="CPF",
            label_msgid=_(u"label_rg"),
            helper_js=('++resource++paciente.js', '++resource++jquery.maskedinput.js', '++resource++validacpf.js'),
        ),
    ),

    atapi.DateTimeField(
        name="nascimento_paciente",
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Data nascimento",
            label_msgid=_(u"label_nascimento"),
            starting_year=1900,
            format='%d-%m-%Y',
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name="uf_nasc_paciente",
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
        searchable=True,
        widget=atapi.SelectionWidget(
            label="Sexo",
            label_msgid=_(u"label_uf_nasc"),
        ),
        vocabulary=["Masculino", "Feminino"]
    ),
    atapi.StringField(
        name="ocupacao_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Ocupação",
            label_msgid=_(u"label_ocupacao"),
        ),
    ),
    atapi.StringField(
        name="formacao_paciente",
        searchable=True,
        widget=atapi.SelectionWidget(
            label="Nível de formação",
            label_msgid=_(u"label_formacao"),
        ),
        vocabulary=['', 'Não informado', 'Analfabeto', 'Ensino Fundamental', 'Ensino Médio',
                    'Profissionalizante', 'Graduação',
                    'Especialização', 'Mestrado', 'Doutorado']
    ),
    atapi.StringField(
        name="tempo_escola_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Quantidade de anos que frequentou escola",
            label_msgid=_(u"label_tempo_escola"),
        ),
    ),
    atapi.StringField(
        name="raca_paciente",
        searchable=True,
        widget=atapi.SelectionWidget(
            label="Raça",
            label_msgid=_(u"label_raca"),
        ),
        vocabulary=['', 'Não informado', 'Branca', 'Preta', 'Parda', 'Indígena', 'Amarela']
    ),
    atapi.StringField(
        name="cep_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="CEP",
            label_msgid=_(u"label_cep"),
            helper_js=('++resource++consultacep.js',),
        ),
    ),
    atapi.StringField(
        name="logradouro_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Endereço",
            label_msgid=_(u"label_end"),
            size=50,
        ),
    ),
    atapi.StringField(
        name="complemento_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Complemento",
            label_msgid=_(u"label_complemento"),
        ),
    ),
    atapi.StringField(
        name="bairro_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Bairro ou Satélite:",
            label_msgid=_(u"label_bairro"),
            size=50,
        ),
    ),
    atapi.StringField(
        name="cidade_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Cidade",
            label_msgid=_(u"label_cidade"),
        ),
    ),
    atapi.StringField(
        name="uf_paciente",
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
        name="fone_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Fone residencial",
            label_msgid=_(u"label_fone"),
        ),
    ),
    atapi.StringField(
        name="cel_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Celular",
            label_msgid=_(u"label_cel"),
        ),
    ),
    atapi.StringField(
        name="nome_parente_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Nome parente ou amigo",
            label_msgid=_(u"label_nome_parente"),
            size=50,
        ),
    ),
    atapi.StringField(
        name="fone_parente_paciente",
        searchable=True,
        widget=atapi.StringWidget(
            label="Fone parente ou amigo",
            label_msgid=_(u"label_fone_parente"),
        ),
    ),
),)

schema['id'].widget.visible['edit'] = 'invisible'
schema['description'].widget.visible['edit'] = 'invisible'
schema['allowDiscussion'].widget.visible['edit'] = 'invisible'
schema['excludeFromNav'].widget.visible['edit'] = 'invisible'
schema['creators'].widget.visible['edit'] = 'invisible'
schema['contributors'].widget.visible['edit'] = 'invisible'
schema['rights'].widget.visible['edit'] = 'invisible'
schema['effectiveDate'].widget.visible['edit'] = 'invisible'
schema['expirationDate'].widget.visible['edit'] = 'invisible'
schema['subject'].widget.visible['edit'] = 'invisible'
schema['relatedItems'].widget.visible['edit'] = 'invisible'
schema['location'].widget.visible['edit'] = 'invisible'
schema['language'].widget.visible['edit'] = 'invisible'
schema['nextPreviousEnabled'].widget.visible['edit'] = 'invisible'

schemata.finalizeATCTSchema(schema)


class Paciente(ATFolder, HistoryAwareMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(IPaciente)

    meta_type = 'Paciente'
    portal_type = 'Paciente'

    _at_rename_after_creation = True
    schema = schema

    def _renameAfterCreation(self, check_auto_id=False):
        """
        """
        normalizer = getUtility(IIDNormalizer)
        titulo = self.prontuario_paciente + '-' + self.title
        newId = normalizer.normalize(titulo)
        #comitar a subtransacao
        transaction.savepoint(optimistic=True)
        self.setId(newId)

    def getIdadePaciente(self):
        try:
            nasc = self.nascimento_paciente
            if nasc:
                nasc = datetime.date(int(nasc.year()), int(nasc.month()), int(nasc.day()))
                idade = datetime.date.today() - nasc
                return idade.days/365
            else:
                return 0
        except:
            pass

atapi.registerType(Paciente, config.PROJECTNAME)

