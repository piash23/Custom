# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Athira P S (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#
##################################################################################
{
    'name': 'Voice Chat In CloudBI Fusion',
    'version': '16.0.1.0.0',
    'category': 'Discuss',
    'summary': 'Voice Message in Fusion Discuss',
    'description': 'Record voice note in CloudBI Fusion,Voice Chat In CloudBI Fusion,Voice Message CloudBI Fusion',
    'author': 'Eqilibrium Solutions',
    'company': 'Eqilibrium  Solutions',
    'maintainer': 'Eqilibrium  Solutions',
    'images': ['static/description/banner.gif'],
    'website': 'https://www.eqilibriumsolutions.com',
    'depends': ['base', 'mail'],
    'assets': {
        'web.assets_backend': [
            'voice_note_in_chatter/static/src/xml/voice_in_odoo.xml',
            'voice_note_in_chatter/static/src/js/record_voice_component.js',
            'voice_note_in_chatter/static/src/js/voice_in_odoo.js',
            'voice_note_in_chatter/static/src/js/record_voice_model.js'
        ]
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
