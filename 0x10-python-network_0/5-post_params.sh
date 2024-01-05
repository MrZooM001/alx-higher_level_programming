#!/bin/bash
# a script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -Is -L "$1" --request POST -H 'email: test@gmail.com' -H 'subject: I will always be here for PLD'
