#!/usr/bin/python3
"""A script that fetches a URL using 'requests' package."""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    req_id = response.headers['X-Request-Id']
    print(req_id)
