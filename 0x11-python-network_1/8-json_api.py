#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request
to a URL with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': (argv[1] if (len(argv) > 1) else "")}
    response = requests.post(url=url, data=payload)
    try:
        res_json = response.json()
        if len(res_json) == 0:
            print('No result')
        else:
            print("[{}] {}".format(res_json['id'], res_json['name']))
    except Exception:
        print("Not a valid JSON")
