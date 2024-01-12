#!/usr/bin/python3
"""A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    res_json = response.json()
    i = 0
    for key in res_json:
        if i < 10:
            sha = res_json[i]['sha']
            author = res_json[i]['commit']['author']['name']
            print("{}: {}".format(sha, author))
        i += 1
