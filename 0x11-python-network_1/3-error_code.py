#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays X-Request-Id variable's value from header of the response"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as respo:
            response = respo.read()
            print(response.decode('utf-8'))
    except HTTPError as ex:
        if hasattr(ex, 'code'):
            print('Error code: {}'.format(ex.code))
