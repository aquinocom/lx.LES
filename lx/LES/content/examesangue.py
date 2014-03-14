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

# Product imports
from lx.LES.interfaces.contents import IExameSangue
from lx.LES import LESMessageFactory as _
from lx.LES import config

schema = ATCTContent.schema.copy()

schema['title'].widget.visible['edit'] = 'invisible'
schema['description'].widget.visible['edit'] = 'invisible'

schemata.finalizeATCTSchema(schema)


class ExameSangue(ATCTContent, HistoryAwareMixin):
    """Exame de sangue
    """

    security = ClassSecurityInfo()

    implements(IExameSangue)

    meta_type = 'ExameSangue'
    portal_type = 'ExameSangue'

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        """
        """
        transaction.commit()
        normalizer = getUtility(IIDNormalizer)
        data_consulta = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        titulo = 'Exame de sangue:  ' + data_consulta
        new_id = normalizer.normalize(titulo)
        self.setTitle(titulo)
        self.setId(new_id)

    def getPacienteExame(self):
        """Retorna qual o paciente está vinculado ao exame
        """
        paciente = self.aq_parent
        return paciente.UID()

    schema = schema

atapi.registerType(ExameSangue, config.PROJECTNAME)
