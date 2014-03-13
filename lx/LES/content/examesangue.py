# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements

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

schemata.finalizeATCTSchema(schema)


class ExameSangue(ATCTContent, HistoryAwareMixin):
    """Exame de sangue
    """

    security = ClassSecurityInfo()

    implements(IExameSangue)

    meta_type = 'ExameSangue'
    portal_type = 'ExameSangue'

    _at_rename_after_creation = True

    schema = schema

atapi.registerType(ExameSangue, config.PROJECTNAME)
