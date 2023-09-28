#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file in the body
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"