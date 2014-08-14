# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner
from plone.memoize.instance import memoize
from datetime import datetime


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
            nome = self.request.get('title', None)
            ocupacao = self.request.get('ocupacao_paciente', None)
            ano_nascimento = self.request.get('nascimento_paciente_year', None)
            mes_nascimento = self.request.get('nascimento_paciente_month', None)
            dia_nascimento = self.request.get('nascimento_paciente_day', None)
            uf_nascimento = self.request.get('uf_nasc_paciente', None)
            
            formacao = self.request.get('formacao_paciente', None)
            raca = self.request.get('raca_paciente', None)

            cep = self.request.get('cep_paciente', None)
            logradouro = self.request.get('logradouro_paciente', None)
            complemento = self.request.get('complemento_paciente', None)
            bairro = self.request.get('bairro_paciente', None)
            cidade = self.request.get('cidade_paciente', None)
            uf = self.request.get('uf_paciente', None)
            
            fone = self.request.get('fone_paciente', None)
            celular = self.request.get('cel_paciente', None)
            nome_parente = self.request.get('nome_parente_paciente', None)
            fone_parente = self.request.get('fone_parente_paciente', None)
            
            if self.validatePaciente(nome, ocupacao, ano_nascimento, mes_nascimento, \
                                     dia_nascimento, formacao, raca, cep, logradouro, complemento, \
                                     bairro, cidade, fone, celular, nome_parente, fone_parente):
                return self.savePaciente(nome, ocupacao, ano_nascimento, mes_nascimento, \
                                        dia_nascimento, uf_nascimento, formacao, raca, cep, logradouro, complemento, \
                                        bairro, cidade, fone, celular, nome_parente, fone_parente, uf)
        if 'form.action.Cancel' in self.request.form:
            self.request.RESPONSE.redirect(self.context.absolute_url())

    def validatePaciente(self, nome, ocupacao, ano_nascimento, mes_nascimento, \
                        dia_nascimento, formacao, raca, cep, logradouro, complemento, \
                        bairro, cidade, fone, celular, nome_parente, fone_parente):
        """Validação
        """
        context = aq_inner(self.context)
        utils = getToolByName(context, 'plone_utils')
        #import pdb; pdb.set_trace()
        if nome == '':
            self.errors['title'] = "O campo é obrigatório."
        if ocupacao == '':
            self.errors['ocupacao_paciente'] = "O campo é obrigatório."
        if (ano_nascimento == '0000') or (mes_nascimento == '00') or (dia_nascimento == '00'):
            self.errors['nascimento_paciente'] = "O campo é obrigatório"
        if formacao == '':
            self.errors['formacao_paciente'] = "O campo é obrigatório."
        if raca == '':
            self.errors['raca_paciente'] = "O campo é obrigatório."
        if cep == '':
            self.errors['cep_paciente'] = "O campo é obrigatório."
        if logradouro == '':
            self.errors['logradouro_paciente'] = "O campo é obrigatório."
        if complemento == '':
            self.errors['complemento_paciente'] = "O campo é obrigatório."
        if bairro == '':
            self.errors['bairro_paciente'] = "O campo é obrigatório."
        if cidade == '':
            self.errors['cidade_paciente'] = "O campo é obrigatório."
        if fone == '':
            self.errors['fone_paciente'] = "O campo é obrigatório."
        if celular == '':
            self.errors['cel_paciente'] = "O campo é obrigatório."
        if nome_parente == '':
            self.errors['nome_parente_paciente'] = "O campo é obrigatório."
        if fone_parente == '':
            self.errors['fone_parente_paciente'] = "O campo é obrigatório."
        # Check for errors
        if self.errors:
            utils.addPortalMessage("Corrija os erros.", type='error')
            return False
        else:
            return True

    def savePaciente(self, nome, ocupacao, ano_nascimento, mes_nascimento, \
                    dia_nascimento, uf_nascimento, formacao, raca, cep, logradouro, complemento, \
                    bairro, cidade, fone, celular, nome_parente, fone_parente, uf):
        """ Alteração dos dados do paciente
        """
        try:
            context = aq_inner(self.context)
            utils = getToolByName(context, 'plone_utils')
            paciente = self.context
            paciente.setTitle(nome)
            paciente.setOcupacao_paciente(ocupacao)
            dt_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
            paciente.setNascimento_paciente(dt_nascimento)
            paciente.setUf_nasc_paciente(uf_nascimento)
            paciente.setFormacao_paciente(formacao)
            paciente.setRaca_paciente(raca)
            paciente.setCep_paciente(cep)
            paciente.setLogradouro_paciente(logradouro)
            paciente.setComplemento_paciente(complemento)
            paciente.setBairro_paciente(bairro)
            paciente.setCidade_paciente(cidade)
            paciente.setFone_paciente(fone)
            paciente.setCel_paciente(celular)
            paciente.setNome_parente_paciente(nome_parente)
            paciente.setFone_parente_paciente(fone_parente)
            paciente.setUf_paciente(uf)            
            paciente.reindexObject()
            msg = 'Os dados do paciente foram alterados.'
            utils.addPortalMessage(msg, type='info')
            self.request.RESPONSE.redirect(self.context.absolute_url())
        except:
            msg = 'Erro na alteração.'
            utils.addPortalMessage(msg, type='error')