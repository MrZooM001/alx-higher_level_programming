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
        response = urlopen(req)
    except HTTPError as ex:
        if hasattr(ex, 'code'):
            print('Error code: {}'.format(ex.code))
    else:
        print(response.read())
