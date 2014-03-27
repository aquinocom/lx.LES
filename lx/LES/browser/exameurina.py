# -*- coding: utf-8 -*-


# Product imports
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

#Plone imports
from plone.memoize.instance import memoize

#Libs imports


# lx.LES imports
from lx.LES.interfaces.contents import IExameUrina
from lx.LES.browser.utils import getFields


class ExameUrinaView(BrowserView):
    """ view do exames de urina do paciente
    """

    @memoize
    def getNomePaciente(self):
        """Retorna o nome do paciente
        """
        nome = self.context.aq_parent.Title()
        return nome

    @memoize
    def getExames(self):
        """Retorna todos os exames de urina do paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_exames = '/'.join(self.context.aq_parent.getPhysicalPath())
        exames = catalog(object_provides=IExameUrina.__identifier__,
                           path=path_exames,
                           sort_on='Date',
                           sort_order='reverse',)
        return exames

    @memoize
    def getFields(self, schemata):
        """Retorna todos os campos do schemata
        """
        return getFields(self, schemata)
