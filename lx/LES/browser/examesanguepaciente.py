# -*- coding: utf-8 -*-


# Product imports
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

#Plone imports
from plone.memoize.instance import memoize

#Libs imports
from DateTime import DateTime

# lx.LES imports
from lx.LES.interfaces.contents import IExameSangue


class ExameSanguePacienteView(BrowserView):
    """ view do exames de sangue do paciente
    """

    __call__ = ViewPageTemplateFile('templates/examesanguepaciente.pt')

    @memoize
    def getExames(self):
        """Retorna todos os exames de sangue do paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_exames = '/'.join(self.context.aq_parent.getPhysicalPath())
        exames = catalog(object_provides=IExameSangue.__identifier__,
                           path=path_exames,
                           sort_on='Date',
                           sort_order='reverse',)
        return exames