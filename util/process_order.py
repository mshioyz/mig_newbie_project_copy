from model.order import Order

def process_order(order) -> Order:
    orderObj = Order(
        order_id = order['order_id'],
        customer_id = order['customer_id'],
        order_volume = order['order_volume'],
        ticker = order['ticker'],
        price = order['price'],
        time_of_order = order['id'], # possible substitute
        order_type = order['order_type']
    )
    return orderObj