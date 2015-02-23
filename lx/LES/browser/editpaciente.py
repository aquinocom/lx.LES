# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner
from plone.memoize.instance import memoize
from datetime import datetime
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer


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
            prontuario = self.request.get('prontuario_paciente', None)
            identificador = self.request.get('identificador_paciente', None)
            cpf = self.request.get('cpf_paciente', None)
            ocupacao = self.request.get('ocupacao_paciente', None)
            ano_nascimento = self.request.get('nascimento_paciente_year', None)
            mes_nascimento = self.request.get('nascimento_paciente_month', None)
            dia_nascimento = self.request.get('nascimento_paciente_day', None)
            uf_nascimento = self.request.get('uf_nasc_paciente', None)
            formacao = self.request.get('formacao_paciente', None)
            tempo_escola = self.request.get('tempo_escola_paciente', None)
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
            if self.validatePaciente(nome, prontuario):
                return self.savePaciente(nome, prontuario, identificador, cpf, ocupacao, ano_nascimento, mes_nascimento, \
                                        dia_nascimento, uf_nascimento, formacao, raca, cep, logradouro, complemento, \
                                        bairro, cidade, fone, celular, nome_parente, fone_parente, uf)
        if 'form.action.Cancel' in self.request.form:
            self.request.RESPONSE.redirect(self.context.absolute_url())

    def validatePaciente(self, nome, prontuario):
        """Validação
        """
        context = aq_inner(self.context)
        utils = getToolByName(context, 'plone_utils')
        if nome == '':
            self.errors['title'] = "O campo é obrigatório."
        if prontuario == '':
            self.errors['prontuario_paciente'] = "O campo é obrigatório."
        #if rg == '':
        #    self.errors['rg_paciente'] = "O campo é obrigatório."
        #if cpf == '':
        #    self.errors['cpf_paciente'] = "O campo é obrigatório."
        #if ocupacao == '':
        #    self.errors['ocupacao_paciente'] = "O campo é obrigatório."
        #if (ano_nascimento == '0000') or (mes_nascimento == '00') or (dia_nascimento == '00'):
        #    self.errors['nascimento_paciente'] = "O campo é obrigatório"
        #if formacao == '':
        #    self.errors['formacao_paciente'] = "O campo é obrigatório."
        #if raca == '':
        #    self.errors['raca_paciente'] = "O campo é obrigatório."
        #if cep == '':
        #    self.errors['cep_paciente'] = "O campo é obrigatório."
        #if logradouro == '':
        #    self.errors['logradouro_paciente'] = "O campo é obrigatório."
        #if complemento == '':
        #    self.errors['complemento_paciente'] = "O campo é obrigatório."
        #if bairro == '':
        #    self.errors['bairro_paciente'] = "O campo é obrigatório."
        #if cidade == '':
        #    self.errors['cidade_paciente'] = "O campo é obrigatório."
        #if fone == '':
        #    self.errors['fone_paciente'] = "O campo é obrigatório."
        #if celular == '':
        #    self.errors['cel_paciente'] = "O campo é obrigatório."
        #if nome_parente == '':
        #    self.errors['nome_parente_paciente'] = "O campo é obrigatório."
        #if fone_parente == '':
        #    self.errors['fone_parente_paciente'] = "O campo é obrigatório."
        # Check for errors
        if self.errors:
            utils.addPortalMessage("Corrija os erros.", type='error')
            return False
        else:
            return True

    def savePaciente(self, nome, prontuario, identificador, cpf, ocupacao, ano_nascimento, mes_nascimento, \
                    dia_nascimento, uf_nascimento, formacao, raca, cep, logradouro, complemento, \
                    bairro, cidade, fone, celular, nome_parente, fone_parente, uf):
        """ Alteração dos dados do paciente
        """
        #try:
        context = aq_inner(self.context)
        utils = getToolByName(context, 'plone_utils')
        paciente = self.context
        normalizer = getUtility(IIDNormalizer)
        newId = normalizer.normalize(prontuario + '-' + nome)
        paciente.setId(newId)
        paciente.setTitle(nome)
        paciente.setIdentificador_paciente(identificador)
        paciente.setProntuario_paciente(prontuario)
        paciente.setCpf_paciente(cpf)
        paciente.setOcupacao_paciente(ocupacao)
        if ano_nascimento != '0000':
            dt_nascimento = datetime(int(ano_nascimento), int(mes_nascimento), int(dia_nascimento))
        else:
            dt_nascimento = None
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
        #except:
        #    msg = 'Erro na alteração.'
        #    utils.addPortalMessage(msg, type='error')
