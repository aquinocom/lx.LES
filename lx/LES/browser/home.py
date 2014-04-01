# -*- coding: utf-8 -*-


# Product imports
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
from Products.CMFCore.permissions import ModifyPortalContent
#Plone imports
from plone.memoize.instance import memoize

#Libs imports


# lx.LES imports
from lx.LES.interfaces.contents import IPaciente


class HomeView(BrowserView):
    """ Home view
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
    def getPacientes(self):
        """Retorna todos os paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        pacientes = catalog(object_provides=IPaciente.__identifier__,
                           sort_on='sortable_title',
                           sort_order='ascending',)
        return pacientes
