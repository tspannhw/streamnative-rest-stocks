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
import base64, json


#### Initial Run, Create Schema

headers = {
    'Authorization': 'Bearer BearerTokenFromStreamNativeCloud',
    'Content-Type': 'application/json',
}

json_data = {
    'type': 'JSON',
    'schema': '{\"type\": \"record\",\n \"name\": \"Stock\",\n \"fields\": [\n  {\n   \"name\": \"symbol\",\n   \"type\": [\n    \"null\",\n    \"string\"\n   ]\n  },\n  {\n   \"name\": \"ts\",\n   \"type\": [\n    \"null\",\n    \"float\"\n   ]\n  },\n  {\n   \"name\": \"currentts\",\n   \"type\": [\n    \"null\",\n    \"float\"\n   ]\n  },\n  {\n   \"name\": \"volume\",\n   \"type\": [\n    \"null\",\n    \"float\"\n   ]\n  },\n  {\n   \"name\": \"price\",\n   \"type\": [\n    \"null\",\n    \"float\"\n   ]\n  },\n  {\n   \"name\": \"tradeconditions\",\n   \"type\": [\n    \"null\",\n    \"string\"\n   ]\n  },\n  {\n   \"name\": \"uuid\",\n   \"type\": [\n    \"null\",\n    \"string\"\n   ]\n  }\n ]\n}',
}

response = requests.post(
    'https://sn-academy.sndevadvocate.snio.cloud/admin/v2/schemas/public/default/stocks/schema',
    headers=headers,
    json=json_data,
)

## Created initial schema
print(response)

#### End Initial Run, Create Schema
