class Order:
    def __init__(self, 
                 order_id: int, 
                 customer_id: int, 
                 order_volume: int, 
                 ticker: str, 
                 price: int, 
                 time_of_order: int, 
                 order_type: str):
        
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_volume = order_volume
        self.ticker = ticker
        self.price = price
        self.time_of_order = time_of_order
        self.order_type = order_type
