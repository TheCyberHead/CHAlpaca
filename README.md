# Alpaca implementation for the brokers module

Also you can use it as an even easier way to use the Alpaca Api:

```
from alpaca import Alpaca
broker = Alpaca(API_KEY, API_SECRET, endpoint)

broker.symbol = 'GOOG'
broker.quantity = 10
response = broker.buy()

print(response)
```
