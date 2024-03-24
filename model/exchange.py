class Exchange: 
    def __init__(self, buy_orders=None, sell_orders=None, order_queue=None):
        self.buy_orders = None
        self.sell_orders = None
        self.order_queue = None