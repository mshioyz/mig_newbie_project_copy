import heapq
import queue

class Exchange: 
    def __init__(self, buy_orders=None, sell_orders=None, order_queue=None):
        self.buy_orders = []
        self.sell_orders = []
        self.order_classification = queue.Queue()

    def add_order(self, order):
        if order.order_classification == 'buy':
            heapq.heappush(self.buy_orders, order)
        elif order.order_classification == 'sell':
            heapq.heappush(self.sell_orders, order)
        else:
            raise ValueError("Invalid value of order classification. order_classification must be 'buy' or 'sell'")

    def match_orders(self):
        while self.buy_orders and self.sell_orders:
            best_buy = self.buy_orders[0]
            best_sell = self.sell_orders[0]
            
            if -best_buy.price >= best_sell.price:
                traded_volume = min(best_buy.order_volume, best_sell.order_volume)
                print(f"Executed trade: {traded_volume} {best_buy.ticker}; BUY {best_buy.ticker} at {-best_buy.price}, SELL {best_sell.ticker} at {best_sell.price}")
                best_buy.order_volume -= traded_volume
                best_sell.order_volume -= traded_volume

                if best_buy.order_volume == 0:
                    heapq.heappop(self.buy_orders)
                if best_sell.order_volume == 0:
                    heapq.heappop(self.sell_orders)

            else:
                break