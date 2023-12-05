from functools import cached_property
import sys
from .input_validator import InputValidator


class OrdersValidator(InputValidator):
    def __init__(self, orders, barcodes):
        self.barcodes = barcodes
        super().__init__(orders)

    @cached_property
    def validation_mask(self):
        self._validation_mask = ~self.input["order_id"].isin(self.barcodes["order_id"])

        return self._validation_mask
