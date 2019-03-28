#!/usr/bin/python3
#Fork from axolx/gist:4eb54de4b8a4714fcda4071ce333da02

import os
import argparse
import requests
import json
from pprint import pprint

# Requires evironment variable UPTIMEROBOT_API_KEY

try:
    API_KEY = os.environ['UPTIMEROBOT_API_KEY']
except KeyError:
    exit('This script requires an UPTIMEROBOT_API_KEY environment variable '
         'with your Uptime Robot API Key.')

DEFAULT_PARAMS = {
    'format': 'json',
    'apiKey': API_KEY,
    'noJsonCallback': 1,
}


def get_monitors():
    """ Get Monitors
    """
    endpoint = 'https://api.uptimerobot.com/getMonitors'
    r = requests.get(endpoint, DEFAULT_PARAMS)
    return r.json()


def get_alert_contacts():
    """ Get Alert Contacts
    """
    endpoint = 'https://api.uptimerobot.com/getAlertContacts'
    r = requests.get(endpoint, DEFAULT_PARAMS)
    return r.json()


def new_monitors():
    """ New Monitor
    """
    monitors = [
        {
            'monitorFriendlyName': 'sitename',
            'monitorURL': 'http://urltomonitor',
        },
    ]
    endpoint = 'https://api.uptimerobot.com/newMonitor'
    result = []
    for monitor in monitors:
        params = monitor.copy()
        params.update(DEFAULT_PARAMS)
        params.update({'monitorType': '1',
                       'monitorAlertContacts': '2395452',})
        r = requests.get(endpoint, params)
        if r.status_code:
            result.append('%s added' % params['monitorURL'])
    return json.dumps(result)

FUNCTION_MAP = {
    'get_monitors': get_monitors,
    'get_alert_contacts': get_alert_contacts,
    'new_monitors': new_monitors,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=FUNCTION_MAP.keys())
    parser.add_argument(
            "--urls",
            action="append",
            help="URLs for the new_monirtors command")

    args = parser.parse_args()
    func = FUNCTION_MAP[args.command]
    pprint(func())


if __name__ == "__main__":
    main()
