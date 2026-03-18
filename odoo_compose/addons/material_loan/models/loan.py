from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Loan(models.Model):
    _name = 'material.loan'
    _description = 'Prestamo de material'

    material_id = fields.Many2one(
        'material.loan.material',
        string="Material",
        required=True,
    )

    student_name = fields.Char(
        string="Alumno",
        required=True,
    )

    date_loan = fields.Date(
        string="Fecha de préstamo",
        default=fields.Date.today,
    )

    date_return = fields.Date(
        string="Fecha de devolución",
    )

    state = fields.Selection(
        [
            ('borrowed', 'Prestado'),
            ('returned', 'Devuelto'),
        ],
        string="Estado",
        default='borrowed',
    )

    def action_return(self):
        for record in self:
            record.state = 'returned'
            record.date_return = fields.Date.today()

    @api.constrains('material_id', 'state')
    def _check_material_available(self):
        for record in self:
            if record.state == 'borrowed':
                material = record.material_id
                # Contar préstamos activos excluyendo el actual
                active_loans = self.search_count([
                    ('material_id', '=', material.id),
                    ('state', '=', 'borrowed'),
                    ('id', '!=', record.id),
                ])
                if active_loans >= material.quantity:
                    raise ValidationError(
                        f"No hay unidades disponibles de '{material.name}'. "
                        f"Cantidad total: {material.quantity}, "
                        f"actualmente prestadas: {active_loans}."
                    )
