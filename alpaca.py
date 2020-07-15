import alpaca_trade_api as api


class Alpaca:
    def __init__(self, API_KEY, API_SECRET, endpoint):
        self.api = api.REST(API_KEY,
                            API_SECRET,
                            api_version='v2',
                            base_url=endpoint)
        self.account = self.api.get_account()
        self.positions = self.api.list_positions()
        self.symbol = 'GOOG'
        self.quantity = 1

    def auth(self):
        pass

    def buy(self):
        answer = self.api.submit_order(symbol = self.symbol,
                                        side = 'buy',
                                        qty = self.quantity,
                                        type = 'market',
                                        time_in_force = 'day')
        return answer

    def sell(self):
        answer = self.api.submit_order(symbol = self.symbol,
                                       side = 'sell',
                                       qty = self.quantity,
                                       type = 'market',
                                       time_in_force = 'day')
        return answer
