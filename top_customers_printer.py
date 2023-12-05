from functools import cached_property


class TopCustomersPrinter:
    def __init__(self, orders):
        self.orders = orders

    def print(self, amount=5):
        print(f"Top {amount} customers:")
        print(self.top_customers(amount).to_string(index=False))

    @cached_property
    def customer_order_counts(self):
        self._customer_order_counts = (
            self.orders.groupby("customer_id")["order_id"]
            .agg(amount_of_tickets="count")
            .reset_index()
        )

        return self._customer_order_counts

    def top_customers(self, amount):
        return self.customer_order_counts.sort_values(
            by="amount_of_tickets", ascending=False
        ).head(amount)
