# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner
from plone.memoize.instance import memoize


class EditPacienteView(BrowserView):
    """
    Edit Paciente
    """

    __call__ = ViewPageTemplateFile('templates/editpaciente.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = {}

    def editpaciente(self):
        if 'form.action.Save' in self.request.form:
            nome = self.request.get('nome', None)
            ocupacao = self.request.get('ocupacao', None)
            if self.validatePaciente(nome, ocupacao):
                return self.savePaciente(nome, ocupacao)
        if 'form.action.Cancel' in self.request.form:
            self.request.RESPONSE.redirect(self.context.absolute_url())

    def validatePaciente(self, nome, ocupacao):
        """Validação
        """
        context = aq_inner(self.context)
        utils = getToolByName(context, 'plone_utils')
        if nome == '':
            self.errors['nome'] = "O campo é obrigatório."
        if ocupacao == '':
            self.errors['ocupacao'] = "O campo é obrigatório."
        # Check for errors
        if self.errors:
            utils.addPortalMessage("Corrija os erros.", type='error')
            return False
        else:
            return True

    def savePaciente(self, nome, ocupacao):
        """ Alteração dos dados do paciente
        """
        try:
            context = aq_inner(self.context)
            utils = getToolByName(context, 'plone_utils')
            paciente = self.context
            paciente.setTitle(nome)
            paciente.setOcupacao_paciente(ocupacao)
            paciente.reindexObject()
            msg = 'Os dados do paciente foram alterados.'
            utils.addPortalMessage(msg, type='info')
            self.request.RESPONSE.redirect(self.context.absolute_url())
        except:
            msg = 'Erro na alteração.'
            utils.addPortalMessage(msg, type='error')