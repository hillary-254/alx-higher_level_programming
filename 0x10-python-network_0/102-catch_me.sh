#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me that triggers the server to respond with "You got me!"
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
