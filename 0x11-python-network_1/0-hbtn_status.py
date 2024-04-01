#!/usr/bin/python3
"""A python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

# URL to fetch data from
url = 'https://alx-intranet.hbtn.io/status'

# Use urllib to open and read the URL
with urllib.request.urlopen(url) as response:
    # Read the body of the response
    body = response.read()

    # Print the type of the body
    print(f"Body response:\n\t- type: {type(body)}")

    # Print the content of the body
    print(f"\t- content: {body}")

    # Decode the body to get a string and print it
    print(f"\t- utf8 content: {body.decode('utf-8')}")
