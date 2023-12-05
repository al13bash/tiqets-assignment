from functools import cached_property
import sys
from .input_validator import InputValidator


class BarcodesValidator(InputValidator):
    def __init__(self, barcodes):
        super().__init__(barcodes)

    @cached_property
    def validation_mask(self):
        self._validation_mask = self.input.duplicated(subset="barcode", keep="first")

        return self._validation_mask
