# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements
from zope.component import getUtility
import transaction

#plone
from plone.i18n.normalizer.interfaces import IIDNormalizer

#Libs
from datetime import datetime

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin

# Product imports
from lx.LES.interfaces.contents import IExameSangue
from lx.LES import LESMessageFactory as _
from lx.LES import config


schema = ATCTContent.schema.copy() + atapi.Schema((
    atapi.DateTimeField(
        name="dt_exame_sangue",
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
        name='hemacias_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Hemácias',
            label_msgid=_(u"label_hemacias_sangue"),
            helper_js=('++resource++sangue.js', '++resource++jquery.maskedinput.js'),
            size=5,
        ),
    ),
    atapi.StringField(
        name='hb_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Hb',
            label_msgid=_(u"label_hb_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='hto_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Hto',
            label_msgid=_(u"label_hto_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='vcm_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='VCM',
            label_msgid=_(u"label_vcm_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='hcm_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='HCM',
            label_msgid=_(u"label_hcm_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='leuco_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Leuco',
            label_msgid=_(u"label_leuco_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='segm_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Segm',
            label_msgid=_(u"label_segm_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='linfo_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Linfo',
            label_msgid=_(u"label_linfo_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='mono_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Mono',
            label_msgid=_(u"label_mono_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='eos_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Eos',
            label_msgid=_(u"label_eos_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='baso_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Baso',
            label_msgid=_(u"label_baso_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='plaq_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Plaq',
            label_msgid=_(u"label_plaq_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='vhs_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='VHS',
            label_msgid=_(u"label_vhs_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='pcr_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='PCR',
            label_msgid=_(u"label_pcr_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='alfa_1gpa_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Alfa 1 GPA',
            label_msgid=_(u"label_alfa_1gpa_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='c3_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='C3',
            label_msgid=_(u"label_c3_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='c4_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='C4',
            label_msgid=_(u"label_c4_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='anti_dna_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Anti-DNA',
            label_msgid=_(u"label_anti_dna_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='alb_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Alb',
            label_msgid=_(u"label_alb_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='glob_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Glob',
            label_msgid=_(u"label_glob_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='cpk_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='CPK',
            label_msgid=_(u"label_cpk_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='ast_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='AST',
            label_msgid=_(u"label_ast_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='alt_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='ALT',
            label_msgid=_(u"label_alt_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='fal_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='FAL',
            label_msgid=_(u"label_fal_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='ggt_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='GGT',
            label_msgid=_(u"label_ggt_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='bb_total_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Bb Total',
            label_msgid=_(u"label_bb_total_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='bb_indir_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Bb indir.',
            label_msgid=_(u"label_bb_indir_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='dhl_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='DHL',
            label_msgid=_(u"label_dhl_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='creatin_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Creatin',
            label_msgid=_(u"label_creatin_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='proteinur_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Proteinúr',
            label_msgid=_(u"label_proteinur_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='dce_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='DCE',
            label_msgid=_(u"label_dce_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='ldl_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='LDL',
            label_msgid=_(u"label_ldl_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='hdl_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='HDL',
            label_msgid=_(u"label_hdl_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='triglic_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Triglic',
            label_msgid=_(u"label_triglic_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='glicose_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Glicose',
            label_msgid=_(u"label_glicose_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='acido_urico_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Ácido Úrico',
            label_msgid=_(u"label_acido_urico_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='ferritina_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Ferritina',
            label_msgid=_(u"label_ferritina_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='ist_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='I.S.T.',
            label_msgid=_(u"label_ist_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='ctif_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='C.T.I.F.',
            label_msgid=_(u"label_ctif_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='tsh_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='TSH',
            label_msgid=_(u"label_tsh_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='na_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Na',
            label_msgid=_(u"label_na_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='k_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='K',
            label_msgid=_(u"label_k_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='calcio_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Cálcio',
            label_msgid=_(u"label_calcio_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='fosforo_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Fósforo',
            label_msgid=_(u"label_fosforo_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='25_vit_d_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='25 Vit. D',
            label_msgid=_(u"label_25_vit_d_sangue"),
            size=5,
        ),
    ),
    atapi.StringField(
        name='calcio_24_sangue',
        #required=True,
        searchable=True,
        widget=atapi.StringWidget(
            label='Cálcio 24',
            label_msgid=_(u"label_calcio_24_sangue"),
            size=5,
        ),
    ),
),)

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

    def getPacienteExame(self):
        """Retorna qual o paciente está vinculado ao exame
        """
        paciente = self.aq_parent
        return paciente.UID()

    schema = schema

atapi.registerType(ExameSangue, config.PROJECTNAME)
