#!/bin/bash
# a script that makes a request that causes the server to respond with a message containing You got me!, in the body of the response
curl -s -L 0.0.0.0:5000/catch_me --request POST -H "Origin: You got me!"
