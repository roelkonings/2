
from odoo import api, fields, models, _


class WebsiteMenu(models.Model):
    """Improve website.menu with adding booleans that drive
    if the menu is displayed when the user is logger or not.
    """

    _inherit = 'website.menu'

    user_logged = fields.Boolean(
        string="User Logged",
        default=True,
        help=_("If checked, "
               "the menu will be displayed when the user is logged "
               "and give access.")
    )

    user_not_logged = fields.Boolean(
        string="User Not Logged",
        default=True,
        help=_("If checked, "
               "the menu will be displayed when the user is not logged "
               "and give access.")
    )

    # @api.one
    def _compute_visible(self):
        """Display the menu item whether the user is logged or not."""
        # super()._compute_visible()
        super(WebsiteMenu, self)._compute_visible()
        for menu in self:
            if not menu.is_visible:
                return

            if self.env.user == self.env.ref('base.public_user'):
                menu.is_visible = menu.user_not_logged
            else:
                menu.is_visible = menu.user_logged
