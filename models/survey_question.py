# -*- coding: utf-8 -*-
from openerp import fields, models
from openerp.tools.translate import _


class SurveyQuestion(models.Model):

    _inherit = 'survey.question'

    type = fields.Selection(
        selection_add=[('image', _('Image'))]
    )
