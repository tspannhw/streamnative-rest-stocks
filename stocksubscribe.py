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

#### Create subscription
headers = {
    'Authorization': 'Bearer bearerTokenFromStreamNativeCloudPage'
}

subid = '{0}'.format(strftime("%M%S",gmtime()))
print(subid)

response = requests.put(
    'https://sn-academy.sndevadvocate.snio.cloud/admin/v2/persistent/public/default/stocks/subscription/stockssub-' + str(subid),
    headers=headers,
    data='')

if response is not None:
    print(response)
