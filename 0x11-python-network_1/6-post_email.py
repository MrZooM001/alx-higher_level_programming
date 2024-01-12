#!/usr/bin/python3
"""A script that fetches a URL using 'requests' package."""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    headers = {'email': argv[2]}
    response = requests.post(url=url, headers=headers)
    req_json = response.json()
    print(req_json['headers']['Email'])
