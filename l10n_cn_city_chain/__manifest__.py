# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2018-now  jeffery9@gmail.com

{
    'name': 'China - City Data',
    'version': '1.8',
    'icon': '/l10n_cn/static/description/icon.png',
    'category': 'Accounting/Localizations',
    'author': 'Jeffery Chen Fan<jeffery9@gmail.com>',
    "excludes": ["l10n_cn_city"],
    'description': """
Includes the following data for the Chinese localization
========================================================

City Data/城市数据

    """,
    'depends': [
        # 'l10n_cn_chain',
        'l10n_cn_standard_latest_chain',
        'base_address_city',
    ],
    'data': [
        'data/res_city_data.xml',
        # 'data/res.city.csv',
        'views/res_partner_views.xml',
    ],
    'license': 'LGPL-3',
}
