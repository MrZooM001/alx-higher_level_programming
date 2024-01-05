#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server will accept
curl -Is -L --request OPTIONS "$1" | awk '/^Allow/ {$1=""; print $0}'
