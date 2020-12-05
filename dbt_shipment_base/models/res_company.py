#  /usr/bin/env python
#  -*- coding: utf-8 -*-

from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class Company(models.Model):
    _inherit = "res.company"

<<<<<<< HEAD
    shipment_picking_type_id = fields.Many2one('stock.picking.type', string="Shipment Picking Type", required=1)
=======
    shipment_picking_type_id = fields.Many2one('stock.picking.type', required=1)
>>>>>>> 93d415eebecb2b9e189e98d9888143c6b801cced
