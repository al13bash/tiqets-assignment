from csv_loader import CsvLoader
from csv_writer import CsvWriter
from validators import BarcodesValidator, OrdersValidator

from top_customers_printer import TopCustomersPrinter
from unused_barcodes_amount_printer import UnusedBarcodesAmountPrinter
from customer_orders_generator import CustomerOrdersGenerator

import argparse

def build_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--orders_path', dest='orders_path', type=str, help='Add orders_path', default="data/orders.csv")
    parser.add_argument('--barcodes_path', dest='barcodes_path', type=str, help='Add barcodes_path', default="data/barcodes.csv")
    parser.add_argument('--top_customers_amount', dest='top_customers_amount', type=int, help='Add top_customers_amount', default=5)
    parser.add_argument('--output_path', dest='output_path', type=str, help='Add output_path', default="data/result.csv")

    return parser.parse_args()

if __name__ == "__main__":
    args = build_args()

    csv_loader = CsvLoader()
    barcodes = BarcodesValidator(
        barcodes=csv_loader.load(args.barcodes_path)
    ).validate()
    orders = OrdersValidator(
        orders=csv_loader.load(args.orders_path), barcodes=barcodes
    ).validate()

    TopCustomersPrinter(orders=orders).print(amount=args.top_customers_amount)

    UnusedBarcodesAmountPrinter(barcodes=barcodes).print()

    customer_orders = CustomerOrdersGenerator(
        orders=orders, barcodes=barcodes
    ).generate()

    CsvWriter().write(data=customer_orders, path=args.output_path)
