# -*- coding: utf-8 -*-
#import of odoo
from odoo import models

class AccountTaxReport(models.TransientModel):
    _inherit = "account.common.report"
    _name = 'account.tax.reports'
    _description = 'Tax Report'

    def _print_report(self, data):
        return self.env.ref('skit_account_reports.action_report_account_tax').report_action(self, data=data)