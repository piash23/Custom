# Copyright 2016 Tecnativa - Jairo Llopis
# Copyright 2017 Tecnativa - Pedro M. Baeza
# Copyright 2019 ForgeFlow S.L. - Lois Rilo <lois.rilo@forgeflow.com>
# 2020 NextERP Romania
# Copyright 2021 Tecnativa - João Marques
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Mail Debrand",
    "summary": """Remove CloudBI branding in sent emails
    Removes anchor <a href eqilibriumsolutions.com togheder with it's parent
    ( for powerd by) form all the templates
    removes any 'CloudBI' that are in tempalte texts > 20characters
    """,
    "version": "16.0.1.0.0",
    "category": "Social Network",
    "website": "https://www.eqilibriumsolutions.com",
    "author": """Eqilibrium Solutions""",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["mail"],
    "development_status": "Production/Stable",
    "maintainers": ["pedrobaeza", "joao-p-marques"],
}
