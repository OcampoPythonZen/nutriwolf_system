# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date, datetime, time, timedelta

RELIGION_OPTIONS = [
    ('ATEISMO', 'ateismo'),
    ('CREYENTE', 'creyente'),
    ('CATOLICISMO', 'catolicismo'),
    ('CRISTIANISMO', 'cristianismo'),
    ('JUDAISMO', 'judaismo'),
    ('ISLAMISMO', 'islamismo'),
    ('BUDISMO', 'budismo'),
    ('HINDUISMO', 'hinduismo'),
    ('NINGUNA', 'ninguna'),
    ('OTRA', 'otra')
]

CIVIL_STATE_OPTIONS = [
    ('SOLTERO(A)', 'soltero'),
    ('COMPROMETIDO(A)', 'comprometido'),
    ('EN RELACION', 'relacion'),
    ('UNION LIBRE', 'union_libre'),
    ('SEPARADO(A)', 'separado'),
    ('DIVORCIADO(A)', 'divorciado'),
    ('VIUDO(A)', 'viudo'),
    ('NOVIAZGO', 'noviazgo'),
    ('OTRA', 'otra')
]

SEX_OPTIONS = [
    ('H', 'hombre'),
    ('M', 'mujer')
]

class Customer(models.Model):
    _inherit = 'res.partner'
    active = fields.Boolean(string = 'Activo', default = True, required = True)
    fisrt_name = fields.Char(string = 'Nombre(s)', required = True)
    last_name = fields.Char(string = 'Apellido(s)', required = True)
    birthday = fields.Date(string = 'Fecha de Nacimiento', required = True, default = date.today())
    address = fields.Text(string = 'Direccion completa', size = 30)
    religion = fields.Selection(string = 'Religión', RELIGION_OPTIONS)
    birth_place = fields.Char(string = 'Lugar de Nacimiento')
    civil_state = fields.Selection(string = 'Estado Civil', CIVIL_STATE_OPTIONS)
    age = fields.Integer(string = 'Edad', size = 2, required = True, compute = '_age_defined', store = True, readonly = True)
    sex = fields.Selection(string = 'Sexo', SEX_OPTIONS, required = True)
    ocupation = fields.Many2one(string = 'Ocupación', 'ocupation', index = True) 
    telephone = fields.Char(string = 'Tel.', size = 8)
    mobile = fields.Char(string = 'Cel.', size = 10, required = True)
    working_hours = fields.Integer(string = 'Horas que labora', size = 2)
    
    @api.depends('birthday')
    def _age_defined(self):
        actual_year = date.today().year
        birth_year = self.birthday.year
        self.age = actual_year - birth_year

class Ocupation(models.Model):
    _name = 'ocupation'
    active = fields.Boolean(string = 'Activa', default = True, required = True)
    disease_name = fields.Char(string = 'Nombre de la Ocupación', required = True)
    created = fields.Date(string = 'Fecha de Creación', default = date.today(), required = True, readonly = True)
    description = fields.Text(string = 'Desc./Notas.')

class Background(models.Model):
    _name = 'background'
    created = fields.Date(string = 'Fecha de Creación', default = date.today(), required = True, readonly = True)
    ocupation = fields.Many2one(string = 'Enfermedad', 'disease', index = True, require = True) 
    ocupation = fields.Many2one(string = 'Familiar quien padece/padecio', 'family', index = True, required = True) 
    ocupation = fields.Many2one(string = 'Condición actual del familiar', 'condition', index = True, required = True)
    
class Disease(models.Model):
    _name = 'disease'
    active = fields.Boolean(string = 'Activa', default = True, required = True)
    disease_name = fields.Char(string = 'Nombre de la Enfermedad', required = True)
    description = fields.Text(string = 'Desc./Notas.')

class FamilyDisease(models.Model):
    _name = 'family'
    active = fields.Boolean(string = 'Activa', default = True, required = True)
    family_name = fields.Char(string = 'Nombre del Familiar que la padece/padecio', required = True)
    description = fields.Text(string = 'Desc./Notas.')

class ConditionDisease(models.Model):
    _name = 'condition'
    active = fields.Boolean(string = 'Activa', default = True, required = True)
    condition_name = fields.Char(string = 'Condición en la que se encuentra', required = True)
    description = fields.Text(string = 'Desc./Notas.')