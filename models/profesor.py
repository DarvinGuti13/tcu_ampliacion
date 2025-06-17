from odoo import models, fields

class Profesor(models.Model):
    _name = 'tcu.profesor'
    _description = 'Profesor encargado del TCU'

    name = fields.Char(string='Nombre completo', required=True)
    departamento = fields.Char(string='Departamento académico')
    user_id = fields.Many2one('res.users', string='Usuario del sistema')
    estudiante_ids = fields.One2many('tcu.estudiante', 'profesor_id', string='Estudiantes asignados')
