#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""
import urllib.parse
import urllib.request
import sys

# Get the URL and email from command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Encode the email data
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')  # Data should be bytes

# Send POST request and read the response
with urllib.request.urlopen(url, data=data) as response:
    # Decode and print the response body (decoded in utf-8)
    body = response.read().decode('utf-8')
    print(body)
