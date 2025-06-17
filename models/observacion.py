from odoo import models, fields
from datetime import date

class ObservacionAcademica(models.Model):
    _name = 'tcu.observacion'
    _description = 'Observación Académica del Estudiante'

    estudiante_id = fields.Many2one('tcu.estudiante', string='Estudiante', required=True)
    fecha = fields.Date(string='Fecha', default=lambda self: date.today())
    comentario = fields.Text(string='Comentario')
    archivo_adjunto = fields.Binary(string='Archivo Adjunto')
    filename = fields.Char(string='Nombre del archivo')  # opcional
