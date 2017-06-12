# -*- coding: utf-8 -*-
from openerp import api, models, fields, exceptions, _
import base64


class SurveyUserInputLine(models.Model):

    _inherit = 'survey.user_input_line'

    @api.constrains('answer_type')
    def _check_answer_type(self):
        ''' Add new answer type to validation function '''
        for uil in self:
            fields_type = {
                'text': bool(uil.value_text),
                'number': (bool(uil.value_number) or uil.value_number == 0),
                'date': bool(uil.value_date),
                'free_text': bool(uil.value_free_text),
                'suggestion': bool(uil.value_suggested),
                'image': bool(uil.value_image),
            }
            if not fields_type.get(uil.answer_type, True):
                raise exceptions.ValidationError(_('The answer must be in the right type'))

    @api.multi
    def save_line_image(self, user_input_id, question, post, answer_tag):
        ''' Add new handler for storing the binary image '''
        vals = {
            'user_input_id': user_input_id,
            'question_id': question.id,
            'survey_id': question.survey_id.id,
            'skipped': False
        }
        # Skip handling if the contents are an empty string. This way
        # an existing image will not get overwritten with an empty one if
        # the user goes back and re-submits without changing the img.
        if answer_tag in post and post.get(answer_tag) != '':

            if type(post[answer_tag].stream) is file:
                photo = base64.b64encode(post[answer_tag].read())
            else:
                photo = base64.encodestring(post[answer_tag].stream.getvalue())

            vals.update({
                'answer_type': 'image',
                'value_image': photo
            })
        else:
            vals.update({
                'answer_type': None,
                'skipped': True
            })
        old_uil = self.search([
            ('user_input_id', '=', user_input_id),
            ('survey_id', '=', question.survey_id.id),
            ('question_id', '=', question.id)
        ])

        if old_uil:
            old_uil.write(vals)
        else:
            old_uil.create(vals)
        return True

    value_image = fields.Binary('Image', attachment=True)
    answer_type = fields.Selection(
        selection_add=[('image', _('Image'))]
    )
