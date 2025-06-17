from odoo import models, fields

class HistorialEstado(models.Model):
    _name = 'tcu.estado_historial'  
    _description = 'Historial de cambios de estado del TCU'

    estudiante_id = fields.Many2one('tcu.estudiante', string='Estudiante', required=True)
    fecha = fields.Datetime(string='Fecha', default=lambda self: fields.Datetime.now())
    estado_anterior = fields.Selection([
        ('solicitado', 'Solicitado'),
        ('revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('ejecucion', 'En Ejecución'),
        ('finalizado', 'Finalizado'),
    ], string='Estado anterior')

    nuevo_estado = fields.Selection([
        ('solicitado', 'Solicitado'),
        ('revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('ejecucion', 'En Ejecución'),
        ('finalizado', 'Finalizado'),
    ], string='Nuevo estado')

    usuario_id = fields.Many2one('res.users', string='Usuario que realizó el cambio', default=lambda self: self.env.user)
