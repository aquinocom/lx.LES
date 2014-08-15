# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from plone.i18n.normalizer import idnormalizer
from lx.LES.interfaces.contents import IPaciente, IAtendimentoMedicina, IExameSangue, IExameUrina
from lx.LES.content.paciente import schema as paciente_schema
from lx.LES.content.atendimento_medicina import schema as atendimento_schema
from lx.LES.content.examesangue import schema as sangue_schema
from lx.LES.content.exameurina import schema as urina_schema
from StringIO import StringIO
import logging

class BaseExportView(object):

    #__call__ = ViewPageTemplateFile('templates/baseexport.pt')

    def __call__(self):
        contexto = self.context
        catalog = getToolByName(contexto, 'portal_catalog')
        out = StringIO()
        log = logging.getLogger('Exportação:')
        #inicializa xml
        print >> out, '<?xml version="1.0"?>'
        print >> out, '<?mso-application progid="Excel.Sheet"?>'
        print >> out, '<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"'
        print >> out, ' xmlns:o="urn:schemas-microsoft-com:office:office"'
        print >> out, ' xmlns:x="urn:schemas-microsoft-com:office:excel"'
        print >> out, ' xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"'
        print >> out, ' xmlns:html="http://www.w3.org/TR/REC-html40">'
        print >> out, ' <DocumentProperties xmlns="urn:schemas-microsoft-com:office:office">'
        print >> out, '  <Author>neips</Author>'
        print >> out, '  <LastAuthor>neips</LastAuthor>'
        print >> out, '  <Created>2014-08-12T13:38:30Z</Created>'
        print >> out, '  <Company>neips</Company>'
        print >> out, '  <Version>11.8132</Version>'
        print >> out, ' </DocumentProperties>'
        print >> out, ' <ExcelWorkbook xmlns="urn:schemas-microsoft-com:office:excel">'
        print >> out, '  <WindowHeight>8580</WindowHeight>'
        print >> out, '  <WindowWidth>15180</WindowWidth>'
        print >> out, '  <WindowTopX>120</WindowTopX>'
        print >> out, '  <WindowTopY>45</WindowTopY>'
        print >> out, '  <ProtectStructure>False</ProtectStructure>'
        print >> out, '  <ProtectWindows>False</ProtectWindows>'
        print >> out, ' </ExcelWorkbook>'
        print >> out, ' <Styles>'
        print >> out, '  <Style ss:ID="Default" ss:Name="Normal">'
        print >> out, '   <Alignment ss:Vertical="Bottom"/>'
        print >> out, '   <Borders/>'
        print >> out, '   <Font/>'
        print >> out, '   <Interior/>'
        print >> out, '   <NumberFormat/>'
        print >> out, '   <Protection/>'
        print >> out, '  </Style>'
        print >> out, ' </Styles>'
        #lista pacientes
        pacientes = catalog(object_provides=IPaciente.__identifier__,)
        if pacientes:
            inutilizados_paciente = ['id', 'title', 'description', 'allowDiscussion', 'excludeFromNav', 'creators',
                         'contributors', 'rights', 'effectiveDate', 'expirationDate',
                         'subject', 'relatedItems', 'location', 'language', 'nextPreviousEnabled',
                         'constrainTypesMode', 'locallyAllowedTypes', 'immediatelyAddableTypes',
                         'creation_date', 'modification_date', 'ocupacao_paciente', 'formacao_paciente',
                         'raca_paciente', 'cep_paciente', 'logradouro_paciente', 'complemento_paciente',
                         'bairro_paciente', 'cidade_paciente', 'uf_paciente', 'fone_paciente',
                         'cel_paciente', 'nome_parente_paciente', 'fone_parente_paciente']
            campos_paciente = paciente_schema.keys()
            [campos_paciente.remove(i) for i in inutilizados_paciente if i in campos_paciente]
            #percorre pacientes para listar atendimentos e exames
            for paciente in pacientes:
                #seta nome na aba
                print >> out, ' <Worksheet ss:Name="%s">' %(paciente.Title)
                #setar tamanho da tabela
                print >> out, '<Table ss:ExpandedColumnCount="999" ss:ExpandedRowCount="999" x:FullColumns="1" x:FullRows="1">'
                print >> out, '<Row><Cell><Data ss:Type="String">Dados Paciente</Data></Cell></Row><Row></Row>'
                #monta cabeçalho com nome dos campos
                print >> out, '<Row>'
                print >> out, '<Cell><Data ss:Type="String">Data</Data></Cell>'
                print >> out, '<Cell><Data ss:Type="String">Nome</Data></Cell>'
                for cp in campos_paciente:
                    label_campo = paciente_schema[cp].widget.label
                    print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo
                print >> out, '</Row>'
                #insere valores do paciente
                print >> out, '<Row>'
                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %paciente.modified.strftime('%d-%m-%Y %H:%M')
                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %(paciente.Title)
                for cp in campos_paciente:
                    if cp != 'nascimento_paciente':
                        print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(paciente,cp)
                    else:
                        print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(paciente,cp).strftime('%d-%m-%Y')
                print >> out, '</Row>'
                print >> out, '<Row></Row>'
                #lista atendimentos médicos
                atendimentos = catalog(object_provides=IAtendimentoMedicina.__identifier__,
                                       path = paciente.getPath())
                if atendimentos:
                    print >> out, '<Row><Cell><Data ss:Type="String">Atendimentos médicos</Data></Cell></Row><Row></Row>'
                    inutilizados_atendimento = ['id', 'title', 'description', 'subject', 'relatedItems', 'location',
                                'language', 'effectiveDate', 'expirationDate', 'creation_date',
                                'modification_date', 'creators', 'contributors', 'rights',
                                'allowDiscussion', 'excludeFromNav']
                    campos_atendimento = atendimento_schema.keys()
                    [campos_atendimento.remove(i) for i in inutilizados_atendimento if i in campos_atendimento]
                    for atendimento in atendimentos:
                        #monta cabeçalho com nome dos campos
                        print >> out, '<Row>'
                        for ca in campos_atendimento:
                            label_campo = atendimento_schema[ca].widget.label
                            print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo
                        print >> out, '</Row>'
                        #insere valores do atendimento
                        print >> out, '<Row>'
                        for ca in campos_atendimento:
                            if atendimento_schema[ca].type != 'datetime':
                                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(atendimento,ca)
                            elif atendimento_schema[ca].type == 'datetime' and getattr(atendimento,ca) is not None:
                                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(atendimento,ca).strftime('%d-%m-%Y %H:%M')
                            else:
                                print >> out, '<Cell><Data ss:Type="String"></Data></Cell>'
                        print >> out, '</Row>'
                        print >> out, '<Row></Row>'

                #lista exames sangue
                exames_sangue = catalog(object_provides=IExameSangue.__identifier__,
                                        path = paciente.getPath())
                if exames_sangue:
                    print >> out, '<Row><Cell><Data ss:Type="String">Exames sangue</Data></Cell></Row><Row></Row>'
                    inutilizados_sangue = ['id', 'title', 'description', 'subject', 'relatedItems', 'location',
                                'language', 'effectiveDate', 'expirationDate', 'creation_date',
                                'modification_date', 'creators', 'contributors', 'rights',
                                'allowDiscussion', 'excludeFromNav']
                    campos_sangue = sangue_schema.keys()
                    [campos_sangue.remove(i) for i in inutilizados_sangue if i in campos_sangue]
                    for exame in exames_sangue:
                        #monta cabeçalho com nome dos campos
                        print >> out, '<Row>'
                        for cs in campos_sangue:
                            label_campo = sangue_schema[cs].widget.label
                            print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo
                        print >> out, '</Row>'
                        #insere valores do exame
                        print >> out, '<Row>'
                        for cs in campos_sangue:
                            if sangue_schema[cs].type != 'datetime':
                                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(exame,cs)
                            elif sangue_schema[cs].type == 'datetime' and getattr(exame,cs) is not None:
                                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(exame,cs).strftime('%d-%m-%Y %H:%M')
                            else:
                                print >> out, '<Cell><Data ss:Type="String"></Data></Cell>'
                        print >> out, '</Row>'
                        print >> out, '<Row></Row>'

                #lista exames urina
                exames_urina = catalog(object_provides=IExameUrina.__identifier__,
                                       path = paciente.getPath())
                if exames_urina:
                    print >> out, '<Row><Cell><Data ss:Type="String">Exames urina</Data></Cell></Row><Row></Row>'
                    inutilizados_urina = ['id', 'title', 'description', 'subject', 'relatedItems', 'location',
                                          'language', 'effectiveDate', 'expirationDate', 'creation_date',
                                          'modification_date', 'creators', 'contributors', 'rights',
                                          'allowDiscussion', 'excludeFromNav']
                    campos_urina = urina_schema.keys()
                    [campos_urina.remove(i) for i in inutilizados_urina if i in campos_urina]
                    for exame in exames_urina:
                        #monta cabeçalho com nome dos campos
                        print >> out, '<Row>'
                        for cu in campos_urina:
                            label_campo = urina_schema[cu].widget.label
                            print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo
                        print >> out, '</Row>'
                        #insere valores do exame
                        print >> out, '<Row>'
                        for cu in campos_urina:
                            if urina_schema[cu].type != 'datetime':
                                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(exame,cu)
                            elif sangue_schema[cs].type == 'datetime' and getattr(exame,cs) is not None:
                                print >> out, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(exame,cu).strftime('%d-%m-%Y %H:%M')
                            else:
                                print >> out, '<Cell><Data ss:Type="String"></Data></Cell>'                            
                        print >> out, '</Row>'
                        print >> out, '<Row></Row>'

                print >> out, '</Table>'

                print >> out, '  <WorksheetOptions xmlns="urn:schemas-microsoft-com:office:excel">'
                print >> out, '   <PageSetup>'
                print >> out, '    <Header x:Margin="0.49212598499999999"/>'
                print >> out, '<Footer x:Margin="0.49212598499999999"/>'
                print >> out, '    <PageMargins x:Bottom="0.984251969" x:Left="0.78740157499999996"'
                print >> out, '     x:Right="0.78740157499999996" x:Top="0.984251969"/>'
                print >> out, '   </PageSetup>'
                print >> out, '   <PROTECTOBJECTS>FALSE</PROTECTOBJECTS>'
                print >> out, '   <PROTECTSCENARIOS>FALSE</PROTECTSCENARIOS>'
                print >> out, '  </WorksheetOptions>'
                print >> out, ' </Worksheet>'
        #finaliza xml
        print >> out, '</Workbook>'
        REQUEST = contexto.REQUEST
        log.info(REQUEST.get('AUTHENTICATED_USER'))        
        RESPONSE = REQUEST.RESPONSE
        RESPONSE.setHeader('Content-type','application/vnd.ms-excel')
        RESPONSE.setHeader('Content-Disposition','attachment;filename=dados_les.xls')

        return out.getvalue()
