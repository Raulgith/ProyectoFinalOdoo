from odoo import models, fields, api


class Material(models.Model):
    _name = 'material.loan.material'
    _description = 'Material del instituto'

    name = fields.Char(string="Nombre", required=True)

    quantity = fields.Integer(
        string="Cantidad total",
        default=1,
    )

    available = fields.Boolean(
        string="Disponible",
        compute='_compute_available',
        store=True,
    )

    loan_ids = fields.One2many(
        'material.loan',
        'material_id',
        string="Préstamos",
    )

    quantity_on_loan = fields.Integer(
        string="Cantidad prestada",
        compute='_compute_available',
        store=True,
    )

    # 🔥 AQUI METES ESTO (campo nuevo)
    total_materials = fields.Integer(
        string="Total materiales",
        compute="_compute_total"
    )

    # 🔥 Y ESTE METODO TAMBIEN
    @api.depends('quantity')
    def _compute_total(self):
        for record in self:
            record.total_materials = record.quantity

    @api.depends('quantity', 'loan_ids', 'loan_ids.state')
    def _compute_available(self):
        for record in self:
            on_loan = len(record.loan_ids.filtered(lambda l: l.state == 'borrowed'))
            record.quantity_on_loan = on_loan
            record.available = (record.quantity - on_loan) > 0