# -*- coding: utf-8 -*-
{
    'name': "Mass Mailing Extension",

    'summary': """
        In This Module, we have provided the REST APIs for the Mailing Module. """,

    'description': """
        <h2>Overview</h2>
        <p>In This Module, we have provided the REST APIs for the Mailing Module. </p>
        <p>For more information, visit our <a href="https://www.oodles.com">website</a>.</p>
    """,
    'author': "Oodles Technology",
    'website': "https://www.oodles.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mass_mailing'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'AGPL-3',  # Use the appropriate license identifier
    'images': [
        'static/description/icon.png',
    ],
}
