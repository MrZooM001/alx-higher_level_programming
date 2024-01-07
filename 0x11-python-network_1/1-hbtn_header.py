#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays X-Request-Id variable's value from header of the response"""
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    with urlopen(req) as respo:
        req_id = respo.headers['X-Request-Id']
        print(req_id)
