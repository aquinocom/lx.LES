# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements
from zope.component import getUtility
import transaction

#plone
from plone.i18n.normalizer.interfaces import IIDNormalizer

#Libs
from datetime import datetime

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.CMFCore.utils import getToolByName

# Product imports
from lx.LES.interfaces.contents import IExameUrina, IAtendimentoMedicina
from lx.LES import LESMessageFactory as _
from lx.LES import config

schema = ATCTContent.schema.copy() + atapi.Schema((
    atapi.StringField(
        name='consulta_referencia',
        required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label='Referente a consulta',
            format='select',
            label_msgid=_(u"label_consulta_referencia"),
        ),
        vocabulary="getAtendimentos",
    ),
    atapi.DateTimeField(
        name="dt_exame_urina",
        required=True,
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Data do exame",
            label_msgid=_(u"label_dt_exame_urina"),
            starting_year=1900,
            format='%d.%m.%Y',
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name='ph_urina',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='pH',
            label_msgid=_(u"label_ph_urina"),
            helper_js=('++resource++urina.js', '++resource++jquery.maskedinput.js'),
            size=5,
        ),
    ),
    atapi.StringField(
        name='dens_urina',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Dens',
            label_msgid=_(u"label_dens_urina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='ced_urina',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='CED',
            label_msgid=_(u"label_ced_urina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='leuco_urina',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Leuco',
            label_msgid=_(u"label_leuco_urina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='hem_urina',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Hem',
            label_msgid=_(u"label_hem_urina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='hb_urina',
        #required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label='Hb',
            label_msgid=_(u"label_hb_urina"),
            format='select',
        ),
        vocabulary=[('', ''), ('-', '-'), ('+', '+'), ('++', '++'), ('+++', '+++')],
    ),
    atapi.StringField(
        name='ptns_urina',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='ptns',
            label_msgid=_(u"label_ptns_urina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='cilindros_urina',
        #required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label='Cilindros',
            label_msgid=_(u"label_cilindros_urina"),
            format='select',
        ),
        vocabulary=[('', ''), ('-', '-'), ('+', '+'), ('++', '++'), ('+++', '+++')],
    ),
    atapi.StringField(
        name='flora_urina',
        #required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label='Flora',
            label_msgid=_(u"label_flora_urina"),
            format='select',
        ),
        vocabulary=[('', ''), ('-', '-'), ('+', '+'), ('++', '++'), ('+++', '+++')],
    ),
    atapi.StringField(
        name='muco_urina',
        #required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label='Muco',
            label_msgid=_(u"label_muco_urina"),
            format='select',
        ),
        vocabulary=[('', ''), ('-', '-'), ('+', '+'), ('++', '++'), ('+++', '+++')],
    ),
    atapi.StringField(
        name='cristais_urina',
        #required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label='Cristais',
            label_msgid=_(u"label_cristais_urina"),
            format='select',
        ),
        vocabulary=[('', ''), ('-', '-'), ('+', '+'), ('++', '++'), ('+++', '+++')],
    ),
    atapi.TextField(
        name='outros_urina',
        ##required=True,
        searchable=True,
        default_content_type='text/plain',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label='Outros',
            label_msgid=_(u"label_outros_urina"),
            rows=10,
            cols=40,
        ),
    ),
    atapi.TextField(
        name='exames_imagem_urina',
        ##required=True,
        searchable=True,
        default_content_type='text/plain',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label='Observações dos exames de imagem',
            label_msgid=_(u"label_exames_imagem_urina"),
            rows=5,
            cols=40,
        ),
    ),
    atapi.TextField(
        name='outros_exames_urina',
        ##required=True,
        searchable=True,
        default_content_type='text/plain',
        allowable_content_types=('text/plain',),
        widget=atapi.TextAreaWidget(
            label='Outros exames',
            label_msgid=_(u"label_outros_exames_urina"),
            rows=5,
            cols=40,
        ),
    ),
),)

schema['id'].widget.visible['edit'] = 'invisible'
schema['title'].widget.visible['edit'] = 'invisible'
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


schemata.finalizeATCTSchema(schema)


class ExameUrina(ATCTContent, HistoryAwareMixin):
    """Exame de urina
    """

    security = ClassSecurityInfo()

    implements(IExameUrina)

    meta_type = 'ExameUrina'
    portal_type = 'ExameUrina'

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        """
        """
        transaction.commit()
        normalizer = getUtility(IIDNormalizer)
        data_consulta = self.dt_exame_urina.strftime('%d/%m/%Y')
        titulo = 'Exame de urina:  ' + data_consulta
        new_id = normalizer.normalize(titulo)
        self.setTitle(titulo)
        self.setId(new_id)

    def getAtendimentos(self):
        paciente = self.aq_parent
        catalog = getToolByName(self, 'portal_catalog')
        atendimentos = catalog(path = '/'.join(paciente.getPhysicalPath()),
                               object_provides=IAtendimentoMedicina.__identifier__,)
        lista= []
        if atendimentos:
            if len(atendimentos) == 1:
                dt_atendimento = atendimentos[0].dt_atendimento.strftime('%d/%m/%Y')
                lista.append('Consulta 1 - %s' %dt_atendimento)
            else:
                lista.append("")
                count=1
                for atendimento in atendimentos:
                    dt_atendimento = atendimento.dt_atendimento.strftime('%d/%m/%Y')
                    item = 'Consulta %s - %s' %(count, dt_atendimento)
                    lista.append(item)
                    count= count + 1
        return lista

    def getPacienteExame(self):
        """Retorna qual o paciente está vinculado ao exame
        """
        paciente = self.aq_parent
        return paciente.UID()

    schema = schema

atapi.registerType(ExameUrina, config.PROJECTNAME)
