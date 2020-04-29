# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Template']


class Template(metaclass=PoolMeta):
    __name__ = 'product.template'
    rohs = fields.Selection([
            ('', ''),
            ('yes', 'Yes'),
            ('no', 'No'),
            ], 'Complies ROHS?')

    @staticmethod
    def default_rohs():
        return ''
