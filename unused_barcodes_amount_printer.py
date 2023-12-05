from functools import cached_property


class UnusedBarcodesAmountPrinter:
    def __init__(self, barcodes):
        self.barcodes = barcodes

    def print(self):
        print("Amount of unused barcodes:")
        print(self.unused_barcodes["barcode"].count())

    @cached_property
    def unused_barcodes(self):
        self._unused_barcodes = self.barcodes[
            self.barcodes["order_id"].isnull() | (self.barcodes["order_id"] == "")
        ]

        return self._unused_barcodes