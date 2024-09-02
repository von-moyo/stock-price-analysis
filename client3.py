import json
import random
import urllib.request

# Define the QUERY format string
QUERY = "http://example.com/api/stocks?random={}"

def getDataPoint(quote):
  """Produce all of the needed values to generate a datapoint."""
  stock = quote['stock']
  bid_price = float(quote['top-bid']['price'])
  ask_price = float(quote['top-ask']['price'])
  price = (bid_price + ask_price) / 2
  return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
  """Returns the ratio of price_a to price_b."""
  if price_b == 0:
    return None  # or return some appropriate value or error message
  return price_a / price_b

if __name__ == "__main__":
  # Query the price once every N seconds.
  N = 10
  for _ in range(N):
    quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
    
    prices = {}
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock] = price
      print("Quoted %s at (bid: %s, ask: %s, price: %s)" % (stock, bid_price, ask_price, price))
    
    # Assuming 'ABC' and 'DEF' are the two stocks you're comparing
    if "ABC" in prices and "DEF" in prices:
      ratio = getRatio(prices["ABC"], prices["DEF"])
      if ratio is not None:
        print("Ratio %s" % ratio)
      else:
        print("Ratio cannot be calculated due to zero division.")
