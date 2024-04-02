#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

# Get the URL from command line arguments
url = sys.argv[1]

# Send GET request to the URL
response = requests.get(url)

# Get the value of the X-Request-Id header if it exists
x_request_id = response.headers.get(X-Request-Id)

if x_request_id:
    print(f'{x_request_id}')
else:
    print('X-Request-Id header not found in the response.')
