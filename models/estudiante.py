from odoo import models, fields, api
from odoo.exceptions import UserError

class Estudiante(models.Model):
    _name = 'tcu.estudiante'
    _description = 'Estudiante del TCU'

    name = fields.Char(string='Nombre completo', required=True)
    carnet = fields.Char(string='Carnet', required=True)
    correo = fields.Char(string='Correo electrónico')
    telefono = fields.Char(string='Teléfono')
    lugar_tcu = fields.Char(string='Lugar donde realiza el TCU')
    periodo = fields.Char(string='Periodo y año')

    user_id = fields.Many2one('res.users', string='Usuario del estudiante')
    profesor_id = fields.Many2one('tcu.profesor', string='Profesor asignado')
    observacion_ids = fields.One2many('tcu.observacion', 'estudiante_id', string='Observaciones académicas')
    historial_ids = fields.One2many('tcu.estado_historial', 'estudiante_id', string='Historial de estados')

    estado_solicitud = fields.Selection([
        ('solicitado', 'Solicitado'),
        ('revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('ejecucion', 'En Ejecución'),
        ('finalizado', 'Finalizado'),
    ], string='Estado del TCU', default='solicitado', readonly=True)

    def cambiar_estado_tcu(self):
        for rec in self:
            nuevo_estado = self.env.context.get('nuevo_estado')
            if not nuevo_estado:
                raise UserError("No se proporcionó un nuevo estado en el contexto.")

            usuario = self.env.user
            if not usuario.has_group('tcu_ampliacion.group_tcu_profesor'):
                raise UserError("Solo los profesores pueden cambiar el estado del TCU.")

            if nuevo_estado not in dict(self._fields['estado_solicitud'].selection).keys():
                raise UserError("Estado no válido.")

            estado_anterior = rec.estado_solicitud
            rec.estado_solicitud = nuevo_estado

            self.env['tcu.estado_historial'].create({
                'estudiante_id': rec.id,
                'fecha': fields.Datetime.now(),
                'estado_anterior': estado_anterior,
                'nuevo_estado': nuevo_estado,
                'usuario_id': usuario.id,
            })

    def print_reporte_estudiante(self):
        return self.env.ref('tcu_ampliacion.action_reporte_estudiante').report_action(self)
    
    
    
    





