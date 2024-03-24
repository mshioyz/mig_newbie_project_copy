import heapq
import queue

class Exchange: 
    def __init__(self, buy_orders=None, sell_orders=None, order_queue=None):
        self.buy_orders = []
        self.sell_orders = []
        self.order_queue = []

    