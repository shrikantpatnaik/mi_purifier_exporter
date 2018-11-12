import time
import json
import sys

from miio import airpurifier

# noinspection PyProtectedMember
from prometheus_client import start_http_server, Gauge, Info

PORT_NUMBER = 8000

status = None

aqi = Gauge('mi_purifier_aqi', 'AQI from Purifier', ['name'])
temp = Gauge('mi_purifier_temp', 'Temperature from Purifier', ['name'])
humidity = Gauge('mi_purifier_humidity', 'humidity from Purifier', ['name'])
filter_life_remaining = Gauge('mi_purifier_filter_life', 'Filter life in percent from Purifier', ['name'])
mode = Info('mi_purifier_status', 'Operational Mode of Purifier', ['name'])


if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        purifiers = json.load(f)

    for purifier in purifiers["purifiers"]:
        purifier["object"] = airpurifier.AirPurifier(ip=purifier["ip"], token=purifier["token"])

    start_http_server(PORT_NUMBER)

    while True:
        time.sleep(1)
        for purifier in purifiers["purifiers"]:
            status = purifier["object"].status()
            aqi.labels(purifier["name"]).set(status.aqi)
            temp.labels(purifier["name"]).set(status.temperature)
            humidity.labels(purifier["name"]).set(status.humidity)
            filter_life_remaining.labels(purifier["name"]).set(status.filter_life_remaining)
            mode.labels(purifier["name"]).info({
                'mode': status.mode.name,
                'filterType': status.filter_type.name
            })
