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
from lx.LES.interfaces.contents import IExameUrina
from lx.LES import LESMessageFactory as _
from lx.LES import config

schema = ATCTContent.schema.copy()

schemata.finalizeATCTSchema(schema)


class ExameUrina(ATCTContent, HistoryAwareMixin):
    """Exame de sangue
    """

    security = ClassSecurityInfo()

    implements(IExameUrina)

    meta_type = 'ExameUrina'
    portal_type = 'ExameUrina'

    _at_rename_after_creation = True

    schema = schema

atapi.registerType(ExameUrina, config.PROJECTNAME)
