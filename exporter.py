import time
import json
import sys

from miio import airpurifier, exceptions

# noinspection PyProtectedMember
from prometheus_client import start_http_server, Gauge, Info

status = None

aqi = Gauge('mi_purifier_aqi', 'AQI from Purifier', ['name'])
temp = Gauge('mi_purifier_temp', 'Temperature from Purifier', ['name'])
humidity = Gauge('mi_purifier_humidity', 'humidity from Purifier', ['name'])
filter_life_remaining = Gauge('mi_purifier_filter_life', 'Filter life in percent from Purifier', ['name'])
mode = Info('mi_purifier_status', 'Operational Mode of Purifier', ['name'])


def exit_with_error(error):
    sys.exit(error)


if __name__ == '__main__':
    port_number = 8000

    if len(sys.argv) < 2:
        exit_with_error("JSON file must be passed as first argument")

    with open(sys.argv[1]) as f:
        purifiers = json.load(f)

    if len(purifiers["purifiers"]) < 1:
        exit_with_error("No purifiers found in JSON File")

    for purifier in purifiers["purifiers"]:
        purifier["object"] = airpurifier.AirPurifier(ip=purifier["ip"], token=purifier["token"])

    if len(sys.argv) > 2:
        port_number = int(sys.argv[2])
    start_http_server(port_number)

    while True:
        time.sleep(1)
        for purifier in purifiers["purifiers"]:
            try:
                status = purifier["object"].status()
                aqi.labels(purifier["name"]).set(status.aqi)
                temp.labels(purifier["name"]).set(status.temperature)
                humidity.labels(purifier["name"]).set(status.humidity)
                filter_life_remaining.labels(purifier["name"]).set(status.filter_life_remaining)
                mode.labels(purifier["name"]).info({
                    'mode': status.mode.name,
                    'filterType': status.filter_type.name
                })
            except exceptions.DeviceException as error:
                pass
            except OSError as error:
                pass
