#!/usr/bin/python3
"""A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.post(url, auth=(argv[1], argv[2]))
    res_json = response.json()
    try:
        response = requests.post(url, auth=(argv[1], argv[2]))
        res_json = response.json()
        print(res_json['id'])
    except Exception:
        print("None")
