class Order:
    def __init__(self, customer_type):
        self.items = []
        self.customer_type = customer_type  # 'regular', 'premium', or 'wholesale'

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        subtotal = sum(item["product"].price * item["quantity"] for item in self.items)

        if self.customer_type == "premium":
            return subtotal * 0.9  # 10% discount
        elif self.customer_type == "wholesale":
            return subtotal * 0.75  # 25% discount
        return subtotal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

### ASSERT OBJECT

class OrderAssert:
    def __init__(self, order):
        self.order = order

    def has_total_price(self, expected_price, tolerance=0.01):
        actual_total = self.order.calculate_total()
        assert abs(actual_total - expected_price) <= tolerance, \
            f"Expected total price to be {expected_price}, but was {actual_total}"
        return self

    def has_item_count(self, expected_count):
        actual_count = sum(item["quantity"] for item in self.order.items)
        assert actual_count == expected_count, \
            f"Expected {expected_count} items in order, but found {actual_count}"
        return self

    def includes_product(self, product_name, quantity):
        matching_items = [
            item for item in self.order.items
            if item["product"].name == product_name and item["quantity"] == quantity
        ]
        assert matching_items, \
            f"Expected order to contain {quantity}x {product_name}"
        return self

def assert_that(order):
    return OrderAssert(order)


def test_premium_customer_order_discount():
    order = Order(customer_type="premium")
    order.add_item(Product("Laptop", 1000), 1)
    order.add_item(Product("Mouse", 20), 2)

    assert_that(order) \
        .has_total_price(936) \
        .has_item_count(3) \
        .includes_product("Laptop", 1) \
        .includes_product("Mouse", 2)


def test_wholesale_customer_order_discount():
    order = Order(customer_type="wholesale")
    order.add_item(Product("Laptop", 1000), 2)

    assert_that(order) \
        .has_total_price(1500) \
        .has_item_count(2) \
        .includes_product("Laptop", 2)
