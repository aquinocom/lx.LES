# -*- coding: utf-8 -*-


# Product imports
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
from Products.CMFCore.permissions import ModifyPortalContent
#Plone imports
from plone.memoize.instance import memoize

#Libs imports


# lx.LES imports
from lx.LES.interfaces.contents import IExameSangue, IExameUrina, IAtendimentoMedicina


class PacienteView(BrowserView):
    """ view do paciente
    """

    @memoize
    def isAlterContent(self, obj):
        """
        """
        sm = getSecurityManager()
        if sm.checkPermission(ModifyPortalContent, obj):
            return True
        else:
            return False

    @memoize
    def getAtendimentosMedicina(self):
        """Retorna todos os atendimentos do paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_atendimentos = '/'.join(self.context.getPhysicalPath())
        atendimentos = catalog(object_provides=IAtendimentoMedicina.__identifier__,
                           path=path_atendimentos,
                           sort_on='Date',
                           sort_order='reverse',)
        return atendimentos

    @memoize
    def getExamesSangue(self):
        """Retorna todos os exames de sangue do paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_exames = '/'.join(self.context.getPhysicalPath())
        exames = catalog(object_provides=IExameSangue.__identifier__,
                           path=path_exames,
                           sort_on='Date',
                           sort_order='reverse',)
        return exames

    @memoize
    def getExamesUrina(self):
        """Retorna todos os exames de urina do paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_exames = '/'.join(self.context.getPhysicalPath())
        exames = catalog(object_provides=IExameUrina.__identifier__,
                           path=path_exames,
                           sort_on='Date',
                           sort_order='reverse',)
        return exames

