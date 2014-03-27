# -*- coding: utf-8 -*-


# Product imports
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

#Plone imports
from plone.memoize.instance import memoize

#Libs imports


# lx.LES imports
from lx.LES.interfaces.contents import IExameSangue
from lx.LES.browser.utils import getFields


class ExameSangueView(BrowserView):
    """ view do exames de sangue do paciente
    """

    @memoize
    def getNomePaciente(self):
        """Retorna o nome do paciente
        """
        nome = self.context.aq_parent.Title()
        return nome

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

    @memoize
    def getFields(self, schemata):
        """Retorna todos os campos do schemata
        """
        return getFields(self, schemata)


class GraficoExameSanguePacienteView(BrowserView):
    """ view do exames de sangue do paciente
    https://developers.google.com/chart/image/docs/chart_params#gcharts_chs
    """

    __call__ = ViewPageTemplateFile('templates/graficoexamesanguepaciente.pt')

    @memoize
    def getExames(self):
        """Retorna todos os exames de sangue do paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_exames = '/'.join(self.context.aq_parent.getPhysicalPath())
        exames = catalog(object_provides=IExameSangue.__identifier__,
                           path=path_exames,
                           sort_on='Date',)
        dic = {
            'Exame': '',
            'legenda': 'Hemácias|Hb|Hto|VCM|HCM|Leuco|Segm|Linfo|Mono|Eos|Baso|Plaq',
            'hemacias': '',
            'hb': '',
            'hto': '',
            'vcm': '',
            'hcm': '',
            'leuco': '',
            'segm': '',
            'linfo': '',
            'mono': '',
            'eos': '',
            'baso': '',
            'plaq': '',
        }
        for exame in exames:
            exame = exame.getObject()
            dic['Exame'] = dic['Exame'] + exame.Title().split(' ')[4] + '-' + exame.Title().split(' ')[6]  + '|'
            dic['hemacias'] = dic['hemacias'] + exame.hemacias_sangue + ','
            dic['hb'] = dic['hb'] + exame.hb_sangue + ','
            dic['hto'] = dic['hto'] + exame.hto_sangue + ','
            dic['vcm'] = dic['vcm'] + exame.vcm_sangue + ','
            dic['hcm'] = dic['hcm'] + exame.hcm_sangue + ','
            dic['leuco'] = dic['leuco'] + exame.leuco_sangue + ','
            dic['segm'] = dic['segm'] + exame.segm_sangue + ','
            dic['linfo'] = dic['linfo'] + exame.linfo_sangue + ','
            dic['mono'] = dic['mono'] + exame.mono_sangue + ','
            dic['eos'] = dic['eos'] + exame.eos_sangue + ','
            dic['baso'] = dic['baso'] + exame.baso_sangue + ','
            dic['plaq'] = dic['plaq'] + exame.plaq_sangue + ','
        return dic
