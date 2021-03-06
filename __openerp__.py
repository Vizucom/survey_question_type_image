# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': '"Image" question type for Surveys',
    'category': 'Survey',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['survey'],
    'description': """
"Image" question type for Surveys
=================================
* A new question type that allows the user to upload an image as an answer
* Uses jQuery's uploadPreview library (http://opoloo.github.io/jquery_upload_preview/) to show a thumbnail of the uploaded image
* Note: created for a very specific use case (only one image per survey, intended for the user to upload their own photo). For more generic use, some fine-tuning is very likely required.
""",
    'data': [
        'views/assets.xml',
        'views/website_survey.xml',
    ],
}
