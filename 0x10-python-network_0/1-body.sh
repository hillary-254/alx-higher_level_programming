#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -s -o /dev/null -w "%{http_code}" "$1" | { read status; [ $status -eq 200 ] && curl -s "$1" || echo ""; }
