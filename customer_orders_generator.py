import pandas as pd


class CustomerOrdersGenerator:
    def __init__(self, barcodes, orders):
        self.barcodes = barcodes
        self.orders = orders

    def generate(self):
        return (
            pd.merge(self.barcodes, self.orders, on="order_id")
            .groupby(["order_id", "customer_id"])["barcode"]
            .agg(list)
            .reset_index()
        )
