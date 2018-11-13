# MiPurifier Prometheus Exporter

A simple exporter that can read a JSON file with Xiaomi air purifiers exposes the data as prometheus metrics.

This is only tested with the Mi Purifier 2S, but should work with any purifier supported by [python-miio](https://python-miio.readthedocs.io/en/latest/).

For help on getting the ip and/or token please look at the [python-miio](https://python-miio.readthedocs.io/en/latest/discovery.html#tokens-from-backups) docs.

If you are on iOS and find a 96 character token, please read the [Decrypting iOS Token](#decrypting-ios-token) section

The format for the JSON file can be seen at [example_purifiers.json](/example_purifiers.json)

## Usage

```bash
pip install -r requirements.txt
 
python exporter.py PATH_TO_JSON
```

## Decrypting iOS Token
```bash
pip install pycrypto

python decrypt_ios_token.py TOKEN
```