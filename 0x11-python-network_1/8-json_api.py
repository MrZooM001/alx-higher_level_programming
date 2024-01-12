#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request
to a URL with the letter as a parameter."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': (argv[1] if (len(argv) == 2) else "") }
    response = requests.post(url=url, data=payload)
    try:
        res_json = response.json()
        if res_json == {}:
            print('No result')
        else:
            print("[{}] {}".format(res_json.get('id'), res_json.get('name')))
    except ValueError:
        print("Not a valid JSON")
