#!/bin/bash
# a script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
code=$(curl -Is "$1" | awk '/^HTTP/ {print $2}')
if [ "$code" -eq '200' ]; then
    curl "$1"
fi
