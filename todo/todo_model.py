# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.multi
    def do_toggle_done(self):
        for task in self:
            if not task.is_done:
               task.is_done = True
               task.name = task.name + ' - Hecho'
        return True
        
    @api.multi
    def do_clear_done(self):
        self.active = False
        return True
