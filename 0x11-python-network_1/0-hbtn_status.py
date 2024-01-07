#!/usr/bin/python3
"""A script that fetches a URL"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as respo:
        response = respo.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)).expandtabs(4))
        print("\t- content: {}".format(response).expandtabs(4))
        print("\t- utf8 content: {}".format(response.decode('utf-8')).expandtabs(4))
