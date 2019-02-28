# -*- coding: utf-8 -*-
from odoo import models, fields, api

class materia(models.Model):

    _name = 'inventario.materia'

    imagen = fields.Binary(string = "Imagen")
    name = fields.Char(string = "Id_Producto", required = True)
    nombre = fields.Char(string = "Nombre", required = True)
    coste = fields.Float(string = "Coste del producto/Kg", required = True)
    descripcion = fields.Text(string = "Descripcion del producto")
    proveedor = fields.Many2one("inventario.proveedor", string = "Proveedor")
    cantidad = fields.Integer(string = "Cantidad en mano")
    _sql_constraints = [('PK_NM', 'unique (name)','Ese id ya existe')]


class proveedor(models.Model):
    _name = 'inventario.proveedor'

    name = fields.Char(string = "Id_Proveedor", required = True)
    nombre = fields.Char(string = "Nombre del proveedor", required = True)
    telefono = fields.Integer(string = "Número de telefono", required = True)
    _sql_constraints = [('PK_NM', 'unique (name)','Ese id ya existe')]

    @api.onchange('telefono')
    def validar_telefono(self):
        if self.telefono:
            match = re.match('[1-9]{9}',self.telefono)
            if match == None:
                raise ValidationError('El numero de telefono tiene que contener 9 digitos\n EJEMPLO: 678540245')

class pedidos(models.Model):
    _name = 'inventario.pedidos'

    name = fields.Char(string = "Referencia", required = True)
    fecha_llegada = fields.Date(string = "Fecha pedido")
    materia = fields.Many2many("inventario.materia", string = "Productos")
    proveedor = fields.Many2one("inventario.proveedor", string = "Proveedor")
    cantidad = fields.Integer(string = "Cantidad pedida" , required = True)

class almacen(models.Model):
    _name = 'inventario.almacen'

    name = fields.Char(string = "Id_Restaurante", required = True)
    encargado = fields.Many2one("inventario.encargado", string = "Encargado", required = True)
    materia = fields.Many2many("inventario.materia", string = "Productos")
    _sql_constraints = [('PK_NM', 'unique (name)','Ese id ya existe')]

class encargado(models.Model):
    _name = 'inventario.encargado'

    name = fields.Char(string = "DNI", required = True)
    nombre = fields.Char(string = "Nombre y Apellido", required = True)


    @api.onchange('name')
    def validate_dni(self):
        if self.name:
            match = re.match('[1-9]{8}[BCDFGHJKLMNPQRSTVXYZ]{1}$', self.name)
            if match == None:
                raise ValidationError('No es un DNI valido')

class inventario(models.Model):
    _name = 'inventario.inventario'

    materia = fields.Many2many("inventario.materia", string = "Productos")
    almacen = fields.Many2one("inventario.almacen", string = "Ubicación")
    cantidad = fields.Integer(string = "Cantidad a mano" , required = True)
