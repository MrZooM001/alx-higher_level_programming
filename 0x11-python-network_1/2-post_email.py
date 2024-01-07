#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays X-Request-Id variable's value from header of the response"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urlencode(values).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as respo:
        response = respo.read()
        print(response.decode('utf-8'))
