#!/usr/bin/python3
"""A python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
import sys

# Get the URL from command line arguments
url = sys.argv[1]

# Send request and read the response headers
response = urllib.request.urlopen(url)
headers = response.info()

# Get the value of the X-Request-Id header if it exists
x_request_id = headers.get('X-Request-Id')
if x_request_id:
    print(f'{x_request_id}')
else:
    print('X-Request-Id header not found in the response.')
