#https://pypi.org/project/websocket_client/
# https://finnhub.io/docs/api/websocket-trades
from time import sleep
from math import isnan
import time
import sys
import datetime
import subprocess
import sys
import os
import traceback
import math
from time import gmtime, strftime
import random, string
import uuid
import socket 
import time
import requests
import websocket, base64, json

headers = {
    'Authorization': 'Bearer BearerToken',
    'Content-Type': 'application/octet-stream',
    'Accept': 'application/json',
}

#### for each finnhub stock websocket message

def on_message(ws, message):
    stocks_dict = json.loads(message)

    try:
        if stocks_dict is not None and "data" in stocks_dict:
            for stockitem in stocks_dict['data']:
                try:
                    if stockitem is not None and stockitem['s'] is not None: 
                        print(stockitem['p'])
                        print("Stock: %s  @ %5.2f" % (stockitem['s'],stockitem['p']))
                        uuid_key = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
                        row = {}
                        row['symbol'] = str(stockitem['s'])
                        row['ts'] = float(stockitem['t'])
                        row['currentts'] = float(strftime("%Y%m%d%H%M%S",gmtime()))
                        row['volume'] = float(stockitem['v'])
                        row['price'] = float(stockitem['p'])
                        row['tradeconditions'] = ','.join(stockitem['c'])
                        row['uuid'] = str(uuid_key)

                        if ( stockitem['s'] != '' ):
                            response = requests.post(
                                'https://sn-academy.sndevadvocate.snio.cloud/admin/rest/topics/v1/persistent/public/default/stocks/message',
                                headers=headers,
                                data=json.dumps(row),
                            )
                            if response is not None:
                                print(response)
                except Exception as e: print(e)
    except Exception as ex:
        print (ex)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed websocket to finnhub ###")
    print(close_status_code)
    print(close_msg)

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"TSLA"}')
    ws.send('{"type":"subscribe","symbol":"AMD"}')
    ws.send('{"type":"subscribe","symbol":"MSFT"}')
    ws.send('{"type":"subscribe","symbol":"GOOG"}')
    ws.send('{"type":"subscribe","symbol":"META"}')
    ws.send('{"type":"subscribe","symbol":"NVDA"}')
    ws.send('{"type":"subscribe","symbol":"CRM"}')
    ws.send('{"type":"subscribe","symbol":"BABA"}')
    ws.send('{"type":"subscribe","symbol":"PYPL"}')
    ws.send('{"type":"subscribe","symbol":"EA"}')
    ws.send('{"type":"subscribe","symbol":"WMT"}')
    ws.send('{"type":"subscribe","symbol":"NKE"}')
    ws.send('{"type":"subscribe","symbol":"BRK.B"}')
    ws.send('{"type":"subscribe","symbol":"GOOGL"}')
    ws.send('{"type":"subscribe","symbol":"UNH"}')
    ws.send('{"type":"subscribe","symbol":"JNJ"}')
    ws.send('{"type":"subscribe","symbol":"XOM"}')
    ws.send('{"type":"subscribe","symbol":"JPM"}')
    ws.send('{"type":"subscribe","symbol":"V"}')
    ws.send('{"type":"subscribe","symbol":"HD"}')
    ws.send('{"type":"subscribe","symbol":"LLY"}')
    ws.send('{"type":"subscribe","symbol":"CVX"}')
    ws.send('{"type":"subscribe","symbol":"ABBV"}')
    ws.send('{"type":"subscribe","symbol":"PEP"}')
    ws.send('{"type":"subscribe","symbol":"BAC"}')
    ws.send('{"type":"subscribe","symbol":"KO"}')
    ws.send('{"type":"subscribe","symbol":"MA"}')
    ws.send('{"type":"subscribe","symbol":"AVGO"}')
    ws.send('{"type":"subscribe","symbol":"TMO"}')
    ws.send('{"type":"subscribe","symbol":"COST"}')
    ws.send('{"type":"subscribe","symbol":"CSCO"}')
    ws.send('{"type":"subscribe","symbol":"MCD"}')
    ws.send('{"type":"subscribe","symbol":"ABT"}')
    ws.send('{"type":"subscribe","symbol":"VZ"}')
    ws.send('{"type":"subscribe","symbol":"DIS"}')
    ws.send('{"type":"subscribe","symbol":"BMY"}')
    ws.send('{"type":"subscribe","symbol":"CMCSA"}')
    ws.send('{"type":"subscribe","symbol":"RTX"}')
    ws.send('{"type":"subscribe","symbol":"HON"}')
    ws.send('{"type":"subscribe","symbol":"IBM"}')
    ws.send('{"type":"subscribe","symbol":"CVS"}')
    ws.send('{"type":"subscribe","symbol":"ORCL"}')
    ws.send('{"type":"subscribe","symbol":"CAT"}')
    ws.send('{"type":"subscribe","symbol":"LOW"}')
    ws.send('{"type":"subscribe","symbol":"BLK"}')
    ws.send('{"type":"subscribe","symbol":"MS"}')
    ws.send('{"type":"subscribe","symbol":"BA"}')
    ws.send('{"type":"subscribe","symbol":"INTC"}')
    ws.send('{"type":"subscribe","symbol":"INTU"}')
    ws.send('{"type":"subscribe","symbol":"CB"}')
    ws.send('{"type":"subscribe","symbol":"TMUS"}')
    ws.send('{"type":"subscribe","symbol":"C"}')
    ws.send('{"type":"subscribe","symbol":"DUK"}')
    ws.send('{"type":"subscribe","symbol":"BDX"}')
    ws.send('{"type":"subscribe","symbol":"SLB"}')
    ws.send('{"type":"subscribe","symbol":"MMM"}')
    ws.send('{"type":"subscribe","symbol":"CL"}')
    ws.send('{"type":"subscribe","symbol":"TGT"}')
    ws.send('{"type":"subscribe","symbol":"MRNA"}')
    ws.send('{"type":"subscribe","symbol":"ICE"}')
    ws.send('{"type":"subscribe","symbol":"USB"}')
    print("openned websocket connection to finnhub")

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=GETYOURFINNHUBTOKEN",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
