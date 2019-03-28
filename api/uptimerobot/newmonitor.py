#!/usr/bin/python3

import os
import json
import sys
import requests

try:
    API_KEY = os.environ['RD_OPTION_API_KEY']
except KeyError:
    exit('This script requires an UPTIMEROBOT_API_KEY environment variable '
         'with your Uptime Robot API Key.')

DEFAULT_ALERT = os.environ['RD_OPTION_ALERT_ID']
FILE = os.environ['RD_FILE_MONITORS']

url = "https://api.uptimerobot.com/v2/newMonitor"

headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
    
MONITORS = open(FILE, "r")
ERROR = 0

for line in MONITORS:
  NAME,URL,SPEC_ALERT,others = line.split(";")
  if SPEC_ALERT != "":
    ALERT = "%s-%s" %(DEFAULT_ALERT,SPEC_ALERT)
  else:
    ALERT = DEFAULT_ALERT
  INFO = "\nNAME: %s - URL: %s - ALERT: %s" %(NAME,URL,ALERT)
  print(INFO)
  payload = "api_key=%s&format=json&type=1&url=%s&friendly_name=%s&alert_contacts=%s" %(API_KEY,URL,NAME,ALERT)
  response = requests.request("POST", url, data=payload, headers=headers)
  output_json = json.loads(response.text)
  if output_json['stat'] != "ok":
    ERROR = ERROR + 1
  print(response.text)

sys.exit(ERROR)
