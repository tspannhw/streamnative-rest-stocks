from time import sleep
from math import isnan
import time
import sys
import datetime
import subprocess
import sys
import os
import traceback
from time import gmtime, strftime
import random, string
import uuid
import time
import requests
import base64, json


# https://github.com/streamnative/sn-pulsar-plugins/tree/master/pulsar-rest
# https://pulsar.apache.org/admin-rest-api/

#### Consume msg
headers = {
    'Authorization': 'Bearer BearerTokenFromStreamnativeCloud',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


while True:

    response = requests.post(
        'https://sn-academy.sndevadvocate.snio.cloud/admin/rest/topics/v1/persistent/public/default/stocks/stockssub-0737/message',
        headers=headers,
        data='')

    if response is not None:
        print(response)
        print(response.status_code)
        print(response.json())    # data to save, display
        print(response.headers)   # header data
        print(response.headers['Date'])
        print(response.headers['broker-address'])
        print(response.headers['X-Pulsar-Message-String-Id'])
        print(response.headers['X-Pulsar-Sequence-Id'])
        print(response.headers['X-Pulsar-Long-Schema-Version'])
        print(response.headers['Content-Length'])
        print(response.headers['X-Pulsar-Message-Id'])
        msgid = str(response.headers['X-Pulsar-Message-Id'])
        print(msgid)
        response2 = requests.put('https://sn-academy.sndevadvocate.snio.cloud/admin/rest/topics/v1/persistent/public/default/stocks/stockssub-0737/message',headers=headers, data=msgid)
        if response2 is not None:
            print(response2)
            print(response2.status_code)
            print(response2.headers)
            print(response2.text)

    sleep(1)
