from model.order import Order

def process_order(order) -> Order:
    orderObj = Order(
        order_id = order['order_id'],
        customer_id = order['customer_id'],
        order_volume = order['order_volume'],
        ticker = order['ticker'],
        price = order['price'] if order["order_classification"] == "sell" else -order["price"],
        time_of_order = order['id'], # respresenting time
        order_type = order['order_type'],
        order_classification = order["order_classification"]
    )
    return orderObj