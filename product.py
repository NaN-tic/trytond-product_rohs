# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Template']

from trytond.modules.product.product import STATES, DEPENDS


class Template:
    __name__ = 'product.template'
    __metaclass__ = PoolMeta

    rohs = fields.Selection([
            ('', ''),
            ('yes', 'Yes'),
            ('no', 'No'),
            ], 'Complies ROHS?', required=True, states=STATES, depends=DEPENDS)

    @staticmethod
    def default_rohs():
        return ''
