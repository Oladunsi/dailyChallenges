import requests 
from datetime import datetime
import time

Bitcoin_API_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1,1027'
ifttt_Webhooks_url = 'https://maker.ifttt.com/trigger/{}/with/key/oE06AzcCETsdFuE-dCDamcUAwvRpC53hV8JDFu9Z3f2'
headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': 'ff69631a-5619-4086-8571-765909bf04cc',
}
BITCOIN_PRICE_THRESHOLD = 38420
ETHEREUM_PRICE_THRESHOLD = 1230

def get_latest_bitcoin_price():
    req = requests.Session()
    req.headers.update(headers)
    try:
        response = req.get(Bitcoin_API_url)
        response_json = response.json()
        BitCoinData = response_json["data"]["1"]
        CoinName =  BitCoinData["name"]
        Coinsymbol = BitCoinData["symbol"]
        Price_in_USD = BitCoinData["quote"]["USD"]["price"]
        EtheriumCoinData = response_json["data"]["1027"]
        EtheriumCoinName =   EtheriumCoinData["name"]
        EtheriumCoinsymbol =  EtheriumCoinData["symbol"]
        EtheriumPrice_in_USD =  EtheriumCoinData["quote"]["USD"]["price"]

        return float(Price_in_USD),float(EtheriumPrice_in_USD)
    except Exception as e:
        return e 

def post_ifttt_webhook(event, value):

    # The data will be sent to IFTTT service
    data = {"value1":value}

    #inserts our desired event
    ifttt_event_url = ifttt_Webhooks_url.format(event)

    # sends a http post request to the webhook to url
    req = requests.post(ifttt_event_url, json=data)
    print("done:", req)

def format_bitcoin_history(arr):
    rows = []
    for history in arr:
        date = history["date"].strftime('%d-%m-%Y %H %M')
        price = history["price"]
        row = "{}:<b>{}</b>".format(date,price)
        rows.append(row)
    return "</br>".join(rows)


def main():
       
    Coin_history = [] # the Coin Bank

    while True:
      bitcoinprice = get_latest_bitcoin_price()[0]
      Ethereumprice = get_latest_bitcoin_price()[1]
      price = "Bitcoin ${0}\nEthereunm ${1}".format(bitcoinprice,Ethereumprice)
      date = datetime.now()
      Coin_history.append({"date":date, "price": price})

      # Send an Emergency notification
      if bitcoinprice < BITCOIN_PRICE_THRESHOLD or Ethereumprice < ETHEREUM_PRICE_THRESHOLD:
        post_ifttt_webhook("bitcoin_price_emergency",price)
        post_ifttt_webhook("Bitcoin_Price_Notifier",price)
      
     """ # Send a Telegram notification Once we have 5 items in our bitcoin_history 
      if len(Coin_history) < 1:
        post_ifttt_webhook("Bitcoin_Price_Notifier",price)
        print(post_ifttt_webhook("Bitcoin_Price_Notifier",price))
        #post_ifttt_webhook("Bitcoin_Price_Notifier",format_bitcoin_history(Coin_history)) 
        # Reset the history
        #Coin_history = []
      # Sleep for 5 minutes
      time.sleep(1 * 60)
"""


if __name__=="__main__":
    main()

