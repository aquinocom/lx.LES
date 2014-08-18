# -*- coding: utf-8 -*-
from lx.LES.interfaces.contents import IPaciente, IAtendimentoMedicina, IExameSangue, IExameUrina
from lx.LES.content.paciente import schema as paciente_schema
from lx.LES.content.atendimento_medicina import schema as atendimento_schema
from lx.LES.content.examesangue import schema as sangue_schema
from lx.LES.content.exameurina import schema as urina_schema

from StringIO import StringIO
import logging
from unicodedata import normalize

from Products.CMFCore.utils import getToolByName


class BaseExportView(object):

    def __call__(self):
        contexto = self.context
        catalog = getToolByName(contexto, 'portal_catalog')
        out = StringIO()
        cad = StringIO()
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
        print >> out, '  <Author>bart</Author>'
        print >> out, '  <LastAuthor>bart</LastAuthor>'
        print >> out, '  <Created>2014-08-17T13:31:57Z</Created>'
        print >> out, '  <Version>14.00</Version>'
        print >> out, ' </DocumentProperties>'
        print >> out, ' <OfficeDocumentSettings xmlns="urn:schemas-microsoft-com:office:office">'
        print >> out, '  <AllowPNG/>'
        print >> out, ' </OfficeDocumentSettings>'
        print >> out, ' <ExcelWorkbook xmlns="urn:schemas-microsoft-com:office:excel">'
        print >> out, '  <WindowHeight>6480</WindowHeight>'
        print >> out, '  <WindowWidth>13395</WindowWidth>'
        print >> out, '  <WindowTopX>480</WindowTopX>'
        print >> out, '  <WindowTopY>90</WindowTopY>'
        print >> out, '  <ProtectStructure>False</ProtectStructure>'
        print >> out, '  <ProtectWindows>False</ProtectWindows>'
        print >> out, ' </ExcelWorkbook>'
        print >> out, ' <Styles>'
        print >> out, '  <Style ss:ID="Default" ss:Name="Normal">'
        print >> out, '   <Alignment ss:Vertical="Bottom"/>'
        print >> out, '   <Borders/>'
        print >> out, '   <Font ss:FontName="Calibri" x:Family="Swiss" ss:Size="11" ss:Color="#000000"/>'
        print >> out, '   <Interior/>'
        print >> out, '   <NumberFormat/>'
        print >> out, '   <Protection/>'
        print >> out, '  </Style>'
        print >> out, '  <Style ss:ID="s62">'
        print >> out, '   <Interior ss:Color="#FFFF00" ss:Pattern="Solid"/>'
        print >> out, '  </Style>'
        print >> out, '  <Style ss:ID="s63">'
        print >> out, '   <Interior ss:Color="#16536E" ss:Pattern="Solid"/>'
        print >> out, '  </Style>'        
        print >> out, ' </Styles>'

        #necessidade de setar nomes das abas
        print >> cad, ' <Worksheet ss:Name="DADOS CADASTRAIS e DEMOGRÁFICOS">'
        print >> cad, '   <Table>'
        hst = StringIO()
        print >> hst, ' <Worksheet ss:Name="HISTÓRICO MÉDICO">'
        print >> hst, '   <Table>'
        urina = StringIO()
        print >> urina, ' <Worksheet ss:Name="URINA">'
        print >> urina, '   <Table>'
        sangue = StringIO()
        print >> sangue, ' <Worksheet ss:Name="SANGUE">'
        print >> sangue, '   <Table>'

        #lista pacientes
        pacientes = catalog(object_provides=IPaciente.__identifier__,)
        if pacientes:
            inutilizados_paciente = ['id', 'title', 'description', 'allowDiscussion',
                                     'excludeFromNav', 'creators', 'contributors', 'rights', 'effectiveDate',
                                     'expirationDate', 'subject', 'relatedItems', 'location', 'language',
                                     'nextPreviousEnabled', 'constrainTypesMode', 'locallyAllowedTypes',
                                     'immediatelyAddableTypes', 'creation_date', 'modification_date']
            campos_paciente = paciente_schema.keys()
            [campos_paciente.remove(i) for i in inutilizados_paciente if i in campos_paciente]
            #gera lista com ids dos pacientes afim de comparar o indice na montagem dos cabecalhos
            ids_pacientes = [paciente.id for paciente in pacientes]
            #ABA DADOS CADASTRAIS
            #monta cabeçalho com nome dos campos
            print >> cad, '<Row>'
            print >> cad, '<Cell ss:StyleID="s62"><Data ss:Type="String">PACIENTE</Data></Cell>'
            print >> cad, '<Cell ss:StyleID="s62"><Data ss:Type="String">DATA</Data></Cell>'
            for campo in campos_paciente:
                label_campo = paciente_schema[campo].widget.label
                label_campo = normalize('NFKD', label_campo.decode('utf-8')).encode('ASCII','ignore')
                print >> cad, '<Cell ss:StyleID="s62"><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo.upper()
            print >> cad, '</Row>'
            #percorre pacientes
            for paciente in pacientes:
                #insere valores do paciente
                print >> cad, '<Row>'
                print >> cad, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %paciente.modified.strftime('%d-%m-%Y %H:%M')
                print >> cad, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %(paciente.Title)
                for campo in campos_paciente:
                    if campo != 'nascimento_paciente':
                        print >> cad, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(paciente, campo)
                    else:
                        print >> cad, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(paciente, campo).strftime('%d-%m-%Y')
                print >> cad, '</Row>'
                #ABA HISTORICO
                #lista atendimentos médicos
                atendimentos = catalog(object_provides=IAtendimentoMedicina.__identifier__, path = paciente.getPath())
                if atendimentos:
                    inutilizados_atendimento = ['id', 'title', 'description', 'subject', 'relatedItems', 'location',
                                'language', 'effectiveDate', 'expirationDate', 'creation_date',
                                'modification_date', 'creators', 'contributors', 'rights',
                                'allowDiscussion', 'excludeFromNav']
                    campos_atendimento = atendimento_schema.keys()
                    [campos_atendimento.remove(i) for i in inutilizados_atendimento if i in campos_atendimento]
                    #monta cabeçalho com nome dos campos
                    #checa indice para montar cabecalho apenas uma vez
                    if ids_pacientes.index(paciente.id) == 0:
                        print >> hst, '<Row>'
                        print >> hst, '<Cell ss:StyleID="s62"><Data ss:Type="String">PACIENTE</Data></Cell>'
                        topo = campos_atendimento * len(atendimentos)
                        for item in topo:
                            label_campo = atendimento_schema[item].widget.label
                            label_campo = normalize('NFKD', label_campo.decode('utf-8')).encode('ASCII','ignore')
                            print >> hst, '<Cell ss:StyleID="s62"><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo.upper()
                            if item == 'conduta':
                                print >> hst, '<Cell ss:StyleID="s63"><Data ss:Type="String"></Data></Cell>'
                        print >> hst, '</Row>'
                    #insere valores do atendimento
                    print >> hst, '<Row>'
                    print >> hst, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %(paciente.Title)
                    for atendimento in atendimentos:
                        for campo in campos_atendimento:
                            if atendimento_schema[campo].type != 'datetime':
                                print >> hst, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(atendimento, campo)
                            elif atendimento_schema[campo].type == 'datetime' and getattr(atendimento, campo) is not None:
                                data = getattr(atendimento, campo).strftime('%d-%m-%Y')
                                print >> hst, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %data
                            else:
                                print >> hst, '<Cell><Data ss:Type="String"></Data></Cell>'
                        print >> hst, '<Cell ss:StyleID="s63"><Data ss:Type="String"></Data></Cell>'
                    print >> hst, '</Row>'
                #ABA URINA
                #lista exames urina
                exames_urina = catalog(object_provides=IExameUrina.__identifier__,
                                       path = paciente.getPath())
                if exames_urina:
                    inutilizados_urina = ['id', 'title', 'description', 'subject', 'relatedItems', 'location',
                                          'language', 'effectiveDate', 'expirationDate', 'creation_date',
                                          'modification_date', 'creators', 'contributors', 'rights',
                                          'allowDiscussion', 'excludeFromNav']
                    campos_urina = urina_schema.keys()
                    [campos_urina.remove(i) for i in inutilizados_urina if i in campos_urina]
                    #monta cabeçalho com nome dos campos
                    #checa indice para montar cabecalho apenas uma vez
                    if ids_pacientes.index(paciente.id) == 0:
                        print >> urina, '<Row>'
                        print >> urina, '<Cell ss:StyleID="s62"><Data ss:Type="String">PACIENTE</Data></Cell>'
                        topo = campos_urina * len(exames_urina)
                        for item in topo:
                            label_campo = urina_schema[item].widget.label
                            label_campo = normalize('NFKD', label_campo.decode('utf-8')).encode('ASCII','ignore')
                            print >> urina, '<Cell ss:StyleID="s62"><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo.upper()
                            if item == 'outros_exames_urina':
                                print >> urina, '<Cell ss:StyleID="s63"><Data ss:Type="String"></Data></Cell>'
                        print >> urina, '</Row>'
                    #insere valores do exame
                    print >> urina, '<Row>'
                    print >> urina, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %(paciente.Title)
                    for exame in exames_urina:
                        for campo in campos_urina:
                            if urina_schema[campo].type != 'datetime':
                                print >> urina, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(exame, campo)
                            elif urina_schema[campo].type == 'datetime' and getattr(exame, campo) is not None:
                                data = getattr(exame, campo).strftime('%d-%m-%Y')
                                print >> urina, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %data
                            else:
                                print >> urina, '<Cell><Data ss:Type="String"></Data></Cell>'
                        print >> urina, '<Cell ss:StyleID="s63"><Data ss:Type="String"></Data></Cell>'
                    print >> urina, '</Row>'
                #ABA SANGUE
                #lista exames sangue
                exames_sangue = catalog(object_provides=IExameSangue.__identifier__,
                                        path = paciente.getPath())
                if exames_sangue:
                    inutilizados_sangue = ['id', 'title', 'description', 'subject', 'relatedItems', 'location',
                                          'language', 'effectiveDate', 'expirationDate', 'creation_date',
                                          'modification_date', 'creators', 'contributors', 'rights',
                                          'allowDiscussion', 'excludeFromNav']
                    campos_sangue = sangue_schema.keys()
                    [campos_sangue.remove(i) for i in inutilizados_sangue if i in campos_sangue]
                    #monta cabeçalho com nome dos campos
                    #checa indice para montar cabecalho apenas uma vez
                    if ids_pacientes.index(paciente.id) == 0:
                        print >> sangue, '<Row>'
                        print >> sangue, '<Cell ss:StyleID="s62"><Data ss:Type="String">PACIENTE</Data></Cell>'
                        topo = campos_sangue * len(exames_sangue)
                        for item in topo:
                            label_campo = sangue_schema[item].widget.label
                            label_campo = normalize('NFKD', label_campo.decode('utf-8')).encode('ASCII','ignore')
                            print >> sangue, '<Cell ss:StyleID="s62"><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %label_campo.upper()
                            if item == 'sangue_tsh':
                                print >> sangue, '<Cell ss:StyleID="s63"><Data ss:Type="String"></Data></Cell>'                            
                        print >> sangue, '</Row>'
                    #insere valores do exame
                    print >> sangue, '<Row>'
                    print >> sangue, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %(paciente.Title)
                    for exame in exames_sangue:
                        for campo in campos_sangue:
                            if sangue_schema[campo].type != 'datetime':
                                print >> sangue, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %getattr(exame, campo)
                            elif sangue_schema[campo].type == 'datetime' and getattr(exame, campo) is not None:
                                data = getattr(exame, campo).strftime('%d-%m-%Y')
                                print >> sangue, '<Cell><Data ss:Type="String"><![CDATA[%s]]></Data></Cell>' %data
                            else:
                                print >> sangue, '<Cell><Data ss:Type="String"></Data></Cell>'
                        print >> sangue, '<Cell ss:StyleID="s63"><Data ss:Type="String"></Data></Cell>'                            
                    print >> sangue, '</Row>'

        #fechamento das abas
        print >> cad, '</Table>'
        print >> cad, '  <WorksheetOptions xmlns="urn:schemas-microsoft-com:office:excel">'
        print >> cad, '   <PageSetup>'
        print >> cad, '    <Header x:Margin="0.31496062000000002"/>'
        print >> cad, '<Footer x:Margin="0.31496062000000002"/>'
        print >> cad, '    <PageMargins x:Bottom="0.984251969" x:Left="0.511811024"'
        print >> cad, '     x:Right="0.511811024" x:Top="0.78740157499999996"/>'
        print >> cad, '   </PageSetup>'
        print >> cad, '   <ProtectObjects>FALSE</ProtectObjects>'
        print >> cad, '   <ProtectScenarios>FALSE</ProtectScenarios>'
        print >> cad, '  </WorksheetOptions>'
        print >> cad, ' </Worksheet>'

        print >> hst, '</Table>'
        print >> hst, '  <WorksheetOptions xmlns="urn:schemas-microsoft-com:office:excel">'
        print >> hst, '   <PageSetup>'
        print >> hst, '    <Header x:Margin="0.31496062000000002"/>'
        print >> hst, '<Footer x:Margin="0.31496062000000002"/>'
        print >> hst, '    <PageMargins x:Bottom="0.984251969" x:Left="0.511811024"'
        print >> hst, '     x:Right="0.511811024" x:Top="0.78740157499999996"/>'
        print >> hst, '   </PageSetup>'
        print >> hst, '   <ProtectObjects>FALSE</ProtectObjects>'
        print >> hst, '   <ProtectScenarios>FALSE</ProtectScenarios>'
        print >> hst, '  </WorksheetOptions>'
        print >> hst, ' </Worksheet>'

        print >> urina, '</Table>'
        print >> urina, '  <WorksheetOptions xmlns="urn:schemas-microsoft-com:office:excel">'
        print >> urina, '   <PageSetup>'
        print >> urina, '    <Header x:Margin="0.31496062000000002"/>'
        print >> urina, '<Footer x:Margin="0.31496062000000002"/>'
        print >> urina, '    <PageMargins x:Bottom="0.984251969" x:Left="0.511811024"'
        print >> urina, '     x:Right="0.511811024" x:Top="0.78740157499999996"/>'
        print >> urina, '   </PageSetup>'
        print >> urina, '   <ProtectObjects>FALSE</ProtectObjects>'
        print >> urina, '   <ProtectScenarios>FALSE</ProtectScenarios>'
        print >> urina, '  </WorksheetOptions>'
        print >> urina, ' </Worksheet>'

        print >> sangue, '</Table>'
        print >> sangue, '  <WorksheetOptions xmlns="urn:schemas-microsoft-com:office:excel">'
        print >> sangue, '   <PageSetup>'
        print >> sangue, '    <Header x:Margin="0.31496062000000002"/>'
        print >> sangue, '<Footer x:Margin="0.31496062000000002"/>'
        print >> sangue, '    <PageMargins x:Bottom="0.984251969" x:Left="0.511811024"'
        print >> sangue, '     x:Right="0.511811024" x:Top="0.78740157499999996"/>'
        print >> sangue, '   </PageSetup>'
        print >> sangue, '   <ProtectObjects>FALSE</ProtectObjects>'
        print >> sangue, '   <ProtectScenarios>FALSE</ProtectScenarios>'
        print >> sangue, '  </WorksheetOptions>'
        print >> sangue, ' </Worksheet>'

        #junta dados das abas cad, hst, urina e sangue
        print >> out, cad.getvalue()
        print >> out, hst.getvalue()
        print >> out, urina.getvalue()
        print >> out, sangue.getvalue()

        #finaliza xml
        print >> out, '</Workbook>'
        REQUEST = contexto.REQUEST
        log.info(REQUEST.get('AUTHENTICATED_USER'))
        RESPONSE = REQUEST.RESPONSE
        RESPONSE.setHeader('Content-type', 'application/vnd.ms-excel')
        #RESPONSE.setHeader('Content-type', 'application/xml')
        RESPONSE.setHeader('Content-Disposition', 'attachment;filename=dados_les.xls')

        return out.getvalue()
