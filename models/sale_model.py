from odoo import api, fields, models
from odoo.exceptions import UserError


class SaleModel(models.Model):
    _inherit = "sale.order"

    approval1 = fields.Boolean(String="Aprroval 1", store=True, tracking=True)
    approval2 = fields.Boolean(String="Aprroval 2", store=True, tracking=True)


    # Variable to check if the user has the previlige to see the product cost or not
    see_approval = fields.Boolean(string="Approval", compute="_check_user_approval_privilege")

    # function to calculate if the user has the previlige to see the product cost or not
    @api.depends("name")
    def _check_user_approval_privilege(self):
        for record in self:
            record.see_approval = record.env.user.has_group("approvals_v17.group_see_approval_user")
