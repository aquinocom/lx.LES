# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements
from zope.component import getUtility
import transaction

#plone
from plone.i18n.normalizer.interfaces import IIDNormalizer

#Libs
#from datetime import datetime

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.CMFCore.utils import getToolByName

# Product imports
from lx.LES.interfaces.contents import IExameSangue, IAtendimentoMedicina
from lx.LES import LESMessageFactory as _
from lx.LES import config


schema = ATCTContent.schema.copy() + atapi.Schema((
    #schemata default
    atapi.StringField(
        name='consulta_referencia',
        required=True,
        searchable=True,
        widget=atapi.SelectionWidget(
            label='Referente a consulta',
            format='select',
            label_msgid=_(u"label_hb_urina"),
        ),
        vocabulary="getAtendimentos",
    ),
    atapi.DateTimeField(
        name='dt_exame_sangue',
        required=True,
        searchable=True,
        widget=atapi.CalendarWidget(
            label="Data do exame",
            label_msgid=_(u"label_dt_exame_sangue"),
            starting_year=1900,
            format='%d.%m.%Y',
            show_hm=False,
        ),
    ),
    atapi.StringField(
        name='sangue_hemacias',
        searchable=True,
        widget=atapi.StringWidget(
            label='Hemácias (00,00)',
            label_msgid=_(u"label_sangue_hemacias"),
            helper_js=('++resource++sangue.js', '++resource++jquery.maskedinput.js'),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hemoglobina',
        searchable=True,
        widget=atapi.StringWidget(
            label='Hemoglobina (00,0)',
            label_msgid=_(u"label_sangue_hemoglobina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hematocrito',
        searchable=True,
        widget=atapi.StringWidget(
            label='Hematócrito (00,0)',
            label_msgid=_(u"label_sangue_hematocrito"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_vcm',
        searchable=True,
        widget=atapi.StringWidget(
            label='Volume Corpuscular Médio (VCM) (00,0)',
            label_msgid=_(u"label_sangue_vcm"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hcm',
        searchable=True,
        widget=atapi.StringWidget(
            label='Hemoglobina Corpuscular Média (HCM) (00,0)',
            label_msgid=_(u"label_sangue_hcm"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_chcm',
        searchable=True,
        widget=atapi.StringWidget(
            label='Concentração de Hemoglobina Corpuscular Média (CHCM) (00,0)',
            label_msgid=_(u"label_sangue_chcm"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_rdw',
        searchable=True,
        widget=atapi.StringWidget(
            label='RDW (00,0)',
            label_msgid=_(u"label_sangue_rdw"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_leucocitos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Leucócitos (00000)',
            label_msgid=_(u"label_sangue_leucocitos"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_basofilos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Basófilos (000)',
            label_msgid=_(u"label_sangue_basofilos"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_eosinofilos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Eosinófilos (000)',
            label_msgid=_(u"label_sangue_eosinofilos"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_mielocitos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Mielócitos (000)',
            label_msgid=_(u"label_sangue_mielocitos"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_metamielocitos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Metamielócitos (000)',
            label_msgid=_(u"label_sangue_metamielocitos"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_bastoes',
        searchable=True,
        widget=atapi.StringWidget(
            label='Bastões (000)',
            label_msgid=_(u"label_sangue_bastoes"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_segmentados',
        searchable=True,
        widget=atapi.StringWidget(
            label='Segmentados (0000)',
            label_msgid=_(u"label_sangue_segmentados"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_linfocitos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Linfócitos (0000)',
            label_msgid=_(u"label_sangue_linfocitos"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_linfocitos_atipicos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Linfócito atípico (000)',
            label_msgid=_(u"label_sangue_"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_monocitos',
        searchable=True,
        widget=atapi.StringWidget(
            label='Monócitos (0000)',
            label_msgid=_(u"label_sangue_monocitos"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_plaquetas',
        searchable=True,
        widget=atapi.StringWidget(
            label='Plaquetas (000000)',
            label_msgid=_(u"label_sangue_plaquetas"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_vpm',
        searchable=True,
        widget=atapi.StringWidget(
            label='Volume Plaquetário Médio (VPM) (00,00)',
            label_msgid=_(u"label_sangue_vpm"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_plaquetocrito',
        searchable=True,
        widget=atapi.StringWidget(
            label='Plaquetócrito (0,000)',
            label_msgid=_(u"label_sangue_plaquetocrito"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_pdw',
        searchable=True,
        widget=atapi.StringWidget(
            label='PDW (00,00)',
            label_msgid=_(u"label_sangue_pdw"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_tempo_protrombina',
        searchable=True,
        widget=atapi.StringWidget(
            label='Tempo de Protrombina (00,00)',
            label_msgid=_(u"label_sangue_tempo_protrombina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_atividade_protombina',
        searchable=True,
        widget=atapi.StringWidget(
            label='Atividade de Protrombina (000,00)',
            label_msgid=_(u"label_sangue_atividade_protombina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_inr',
        searchable=True,
        widget=atapi.StringWidget(
            label='I.N.R. (0,00)',
            label_msgid=_(u"label_sangue_inr"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_isi',
        searchable=True,
        widget=atapi.StringWidget(
            label='ISI (0,00)',
            label_msgid=_(u"label_sangue_isi"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_tempo_tromboplastina_parcial',
        searchable=True,
        widget=atapi.StringWidget(
            label='Tempo de Tromboplastina Parcial (00,0)',
            label_msgid=_(u"label_sangue_tempo_tromboplastina_parcial"),
            size=5,
        ),
    ),
    #schemata bioquimica
    atapi.StringField(
        name='sangue_ureia',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Uréia (00,0)',
            label_msgid=_(u"label_sangue_ureia"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_creatinina',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Creatinina (0,00)',
            label_msgid=_(u"label_sangue_creatinina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_acido_urico',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Ácido úrico (0,00)',
            label_msgid=_(u"label_sangue_acido_urico"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_sodio',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Sódio (Na) (000,0)',
            label_msgid=_(u"label_sangue_sodio"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_potassio',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Potássio (K) (0,0)',
            label_msgid=_(u"label_sangue_potassio"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_cloro',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Cloro (Cl) (00,00)',
            label_msgid=_(u"label_sangue_cloro"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_magnesio',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Magnésio (0,0)',
            label_msgid=_(u"label_sangue_magnesio"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_fosforo',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Fósforo (P) (0,0)',
            label_msgid=_(u"label_sangue_fosforo"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_zinco',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Zinco (00,0)',
            label_msgid=_(u"label_sangue_zinco"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_fosfatase_alcalina',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Fosfatase Alcalina (000,0)',
            label_msgid=_(u"label_sangue_fosfatase_alcalina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_alfa_amilase',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Alfa Amilase (000,0)',
            label_msgid=_(u"label_sangue_alfa_amilase"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_lipase',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Lipase (00,0)',
            label_msgid=_(u"label_sangue_lipase"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_ferro_serico',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Ferro Sérico (000,00)',
            label_msgid=_(u"label_sangue_ferro_serico"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_calcio',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Cálcio (Ca) (00,0)',
            label_msgid=_(u"label_sangue_calcio"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_vitamina_c',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Vitamina C (00,0)',
            label_msgid=_(u"label_sangue_vitamina_c"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hidroxivitamina_d',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Hidroxivitamina D (00,00)',
            label_msgid=_(u"label_sangue_hidroxivitamina_d"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_caroteno',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Caroteno (00,00)',
            label_msgid=_(u"label_sangue_caroteno"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_vitamina_a',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Vitamina A (00,00)',
            label_msgid=_(u"label_sangue_vitamina_a"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_vitamina_b12',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Vitamina B12 (000)',
            label_msgid=_(u"label_sangue_vitamina_b12"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_vitamina_e',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Vitamina E (000)',
            label_msgid=_(u"label_sangue_vitamina_e"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_acido_folico',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Ácido Fólico (000)',
            label_msgid=_(u"label_sangue_acido_folico"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_cobre',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Cobre (Cu) (00,00)',
            label_msgid=_(u"label_sangue_cobre"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_tgo_ast',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='TGO - Transaminase Oxalacética (AST) (00,00)',
            label_msgid=_(u"label_sangue_tgo_ast"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_tgp_alt',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='TGP - Transaminase Pirúvica (ALT) (00,00)',
            label_msgid=_(u"label_sangue_tgp_alt"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_ggt',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='GGT - Gama Glutamil Transferase (00,00)',
            label_msgid=_(u"label_sangue_ggt"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_glicose',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Glicose (000)',
            label_msgid=_(u"label_sangue_glicose"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_homocisteina',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Homocisteína (000)',
            label_msgid=_(u"label_sangue_homocisteina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_proteinas_totais',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Proteínas Totais (0,0)',
            label_msgid=_(u"label_sangue_proteinas_totais"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_albumina',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Albumina (0,0)',
            label_msgid=_(u"label_sangue_albumina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_globulinas',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Globulinas (0,0)',
            label_msgid=_(u"label_sangue_globulinas"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_relacao_ag',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Relação A/G (0,0)',
            label_msgid=_(u"label_sangue_relacao_ag"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_colesterol_total',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Colesterol total (000)',
            label_msgid=_(u"label_sangue_colesterol_total"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_triglicerides',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Triglicérides (000)',
            label_msgid=_(u"label_sangue_triglicerides"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_colesterol_hdl',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Colesterol HDL (00)',
            label_msgid=_(u"label_sangue_colesterol_hdl"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_colesterol_vldl',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Colesterol VLDL (00)',
            label_msgid=_(u"label_sangue_colesterol_vldl"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_colesterol_ldl',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Colesterol LDL (000)',
            label_msgid=_(u"label_sangue_colesterol_ldl"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_bilirrubina_total',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Total (0,00)',
            label_msgid=_(u"label_sangue_bilirrubina_total"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_bilirrubina_direta',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Direta (0,00)',
            label_msgid=_(u"label_sangue_bilirrubina_direta"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_bilirrubina_indireta',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Indireta (0,00)',
            label_msgid=_(u"label_sangue_bilirrubina_indireta"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_glicose_basal',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Basal (000)',
            label_msgid=_(u"label_sangue_glicose_basal"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_glicose_30min',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='30 Minutos (000)',
            label_msgid=_(u"label_sangue_glicose_30min"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_glicose_60min',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='60 Minutos (000)',
            label_msgid=_(u"label_sangue_glicose_60min"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_glicose_120min',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='120 Minutos (000)',
            label_msgid=_(u"label_sangue_glicose_120min"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hba1c',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='HbA1c (0,0)',
            label_msgid=_(u"label_sangue_hba1c"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hba1c_labil',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Hba1c Labil (0,0)',
            label_msgid=_(u"label_sangue_hba1c_labil"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hba1a',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='HbA1a (0,0)',
            label_msgid=_(u"label_sangue_hba1a"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hba1b',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='HbA1b (0,0)',
            label_msgid=_(u"label_sangue_hba1b"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hba',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='HbA (00,0)',
            label_msgid=_(u"label_sangue_hba"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_hbf',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='HbF (0,0)',
            label_msgid=_(u"label_sangue_hbf"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_glicemia_media',
        searchable=True,
        schemata='bioquimica',
        widget=atapi.StringWidget(
            label='Glicemia média estimada (000,00)',
            label_msgid=_(u"label_sangue_glicemia_media"),
            size=5,
        ),
    ),
    #schemata imunologia
    atapi.StringField(
        name='sangue_vhs_hemossedimentação',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='VHS - Hemossedimentação (00)',
            label_msgid=_(u"label_sangue_vhs_hemossedimentação"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_cardiolipina_igg',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Cardiolipina IgG, Auto Anticorpos',
            label_msgid=_(u"label_sangue_cardiolipina_igg"),
            description=_(u"Formato >00,0 ou <00,0"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_cardiolipina_igm',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Cardiolipina IgM, Auto Anticorpos',
            label_msgid=_(u"label_sangue_cardiolipina_igm"),
            description=_(u"Formato >00,0 ou <00,0"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_c3',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='C3 (000,0)',
            label_msgid=_(u"label_sangue_c3"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_c4',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='C4 (00,00)',
            label_msgid=_(u"label_sangue_c4"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_anti_ssa',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Anti SSA (000)',
            label_msgid=_(u"label_sangue_anti_ssa"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_anti_ssb',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Anti SSB (000)',
            label_msgid=_(u"label_sangue_anti_ssb"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_anti_rnp',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Anti RNP (000)',
            label_msgid=_(u"label_sangue_anti_rnp"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_anti_sm',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Anti SM (000)',
            label_msgid=_(u"label_sangue_anti_sm"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_anti_dna',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Anti DNA (000)',
            label_msgid=_(u"label_sangue_anti_dna"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_fator_reumatoide',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Fator Reumatóide (FR) (00,0)',
            label_msgid=_(u"label_sangue_fator_reumatoide"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_ige_total',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='IgE Total - imunoglobulina E (0,0)',
            label_msgid=_(u"label_sangue_ige_total"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_pcr',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='PCR - Proteína C Reativa (0,00)',
            label_msgid=_(u"label_sangue_pcr"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_aso',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='ASO - Antiestreptolisina "O" (00)',
            label_msgid=_(u"label_sangue_aso"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_anti_peroxidase',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Anticorpo Anti-Peroxidase da Tireóide (Anti-TPO Microssomal) (00,00)',
            label_msgid=_(u"label_sangue_anti_peroxidase"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_imunoglobulina_iga',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Imunoglobulina IgA (000)',
            label_msgid=_(u"label_sangue_imunoglobulina_iga"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_proteina_c',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Proteína C Reativa Quantitativa (Ultra Sensível) (0,00)',
            label_msgid=_(u"label_sangue_proteina_c"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_anti_tireoglobulina',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Anticorpos Anti Tireoglobulina (00,00)',
            label_msgid=_(u"label_sangue_anti_tireoglobulina"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_waller_rose',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Reação de Waaler Rose',
            label_msgid=_(u"label_sangue_waller_rose"),
            format='select',
        ),
        vocabulary=[("", ""), ('negativo', 'Negativo'), ('positivo', 'Positivo')],
        #vocabulary=[('negativo', 'Negativo'), ('positivo', 'Positivo')],
    ),
    atapi.StringField(
        name='sangue_hepatite_c',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Hepatite C - Anti-HCV',
            label_msgid=_(u"label_sangue_hepatite_c"),
            format='select',
        ),
        vocabulary=[("", ""), ('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
        #vocabulary=[('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
    ),
    atapi.StringField(
        name='sangue_hepatite_b',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Hepatite B - Anti-HBV',
            label_msgid=_(u"label_sangue_hepatite_b"),
            format='select',
        ),
        vocabulary=[("", ""), ('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
        #vocabulary=[('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
    ),
    atapi.StringField(
        name='sangue_citomegalovirus_igg',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Citomegalovírus IgG (000,0)',
            label_msgid=_(u"label_sangue_citomegalovirus_igg"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_citomegalovirus_igm',
        searchable=True,
        schemata='imunologia',
        widget=atapi.StringWidget(
            label='Citomegalovírus IgM (0,00)',
            label_msgid=_(u"label_sangue_citomegalovirus_igm"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_nucleo',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Núcleo',
            label_msgid=_(u"label_sangue_nucleo"),
            format='select',
        ),
        vocabulary=[("", ""), ('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
        #vocabulary=[('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
    ),
    atapi.StringField(
        name='sangue_nucleolo',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Nucléolo',
            label_msgid=_(u"label_sangue_nucleolo"),
            format='select',
        ),
        vocabulary=[("", ""), ('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
        #vocabulary=[('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
    ),
    atapi.StringField(
        name='sangue_citoplasma',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Citoplasma',
            label_msgid=_(u"label_sangue_citoplasma"),
            format='select',
        ),
        vocabulary=[("", ""), ('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
        #vocabulary=[('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
    ),
    atapi.StringField(
        name='sangue_aparelho_mitotico',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Aparelho Mitótico',
            label_msgid=_(u"label_sangue_aparelho_mitotico"),
            format='select',
        ),
        vocabulary=[("", ""), ('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
        #vocabulary=[('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
    ),
    atapi.StringField(
        name='sangue_placa_metafasica',
        searchable=True,
        schemata='imunologia',
        widget=atapi.SelectionWidget(
            label='Placa Metafásica Cromossômica',
            label_msgid=_(u"label_sangue_placa_metafasica"),
            format='select',
        ),
        vocabulary=[("", ""), ('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
        #vocabulary=[('nao-reagente', 'Não reagente'), ('reagente', 'Reagente')],
    ),
    #schemata hormonios
    atapi.StringField(
        name='sangue_t3',
        searchable=True,
        schemata='hormonios',
        widget=atapi.StringWidget(
            label='T3 (Triiodotironina) (00)',
            label_msgid=_(u"label_sangue_t3"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_t4',
        searchable=True,
        schemata='hormonios',
        widget=atapi.StringWidget(
            label='T4 (Tiroxina) (0,0)',
            label_msgid=_(u"label_sangue_t4"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_t4_livre',
        searchable=True,
        schemata='hormonios',
        widget=atapi.StringWidget(
            label='T4 Livre (00)',
            label_msgid=_(u"label_sangue_t4_livre"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='sangue_tsh',
        searchable=True,
        schemata='hormonios',
        widget=atapi.StringWidget(
            label='THS - Hormônio Tireoestimulante Ultra Sensivel (0,00)',
            label_msgid=_(u"label_sangue_tsh"),
            size=5,
        ),
    ),
),)

schema['id'].widget.visible['edit'] = 'invisible'
schema['title'].widget.visible['edit'] = 'invisible'
schema['description'].widget.visible['edit'] = 'invisible'
schema['allowDiscussion'].widget.visible['edit'] = 'invisible'
schema['excludeFromNav'].widget.visible['edit'] = 'invisible'
schema['creators'].widget.visible['edit'] = 'invisible'
schema['contributors'].widget.visible['edit'] = 'invisible'
schema['rights'].widget.visible['edit'] = 'invisible'
schema['effectiveDate'].widget.visible['edit'] = 'invisible'
schema['expirationDate'].widget.visible['edit'] = 'invisible'
schema['subject'].widget.visible['edit'] = 'invisible'
schema['relatedItems'].widget.visible['edit'] = 'invisible'
schema['location'].widget.visible['edit'] = 'invisible'
schema['language'].widget.visible['edit'] = 'invisible'


schemata.finalizeATCTSchema(schema)


class ExameSangue(ATCTContent, HistoryAwareMixin):
    """Exame de sangue
    """

    security = ClassSecurityInfo()

    implements(IExameSangue)

    meta_type = 'ExameSangue'
    portal_type = 'ExameSangue'

    _at_rename_after_creation = True
    schema = schema

    def _renameAfterCreation(self, check_auto_id=False):
        """
        """
        transaction.commit()
        normalizer = getUtility(IIDNormalizer)
        data_consulta = self.dt_exame_sangue.strftime('%d/%m/%Y')
        titulo = 'Exame de sangue:  ' + data_consulta
        new_id = normalizer.normalize(titulo)
        self.setTitle(titulo)
        self.setId(new_id)

    def getAtendimentos(self):
        paciente = self.aq_parent
        catalog = getToolByName(self, 'portal_catalog')
        atendimentos = catalog(path='/'.join(paciente.getPhysicalPath()),
                               object_provides=IAtendimentoMedicina.__identifier__,)
        lista = []
        if atendimentos:
            if len(atendimentos) == 1:
                dt_atendimento = atendimentos[0].dt_atendimento.strftime('%d/%m/%Y')
                lista.append('Consulta 1 - %s' % dt_atendimento)
            else:
                lista.append("")
                count = 1
                for atendimento in atendimentos:
                    dt_atendimento = atendimento.dt_atendimento.strftime('%d/%m/%Y')
                    item = 'Consulta %s - %s' % (count, dt_atendimento)
                    lista.append(item)
                    count = count + 1
        return lista

    def getPacienteExame(self):
        """Retorna qual o paciente está vinculado ao exame
        """
        paciente = self.aq_parent
        return paciente.UID()

atapi.registerType(ExameSangue, config.PROJECTNAME)
