# MiPurifier Prometheus Exporter

A simple exporter that can read a JSON file with Xiaomi air purifiers exposes the data as prometheus metrics.

This is only tested with the Mi Purifier 2S, but should work with any purifier supported by [python-miio](https://python-miio.readthedocs.io/en/latest/).

For help on getting the ip and/or token please look at the [python-miio](https://python-miio.readthedocs.io/en/latest/discovery.html#tokens-from-backups) docs.


##Usage

```bash
python exporter.py purifiers.json
```

