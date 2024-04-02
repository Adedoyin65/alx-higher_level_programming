#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8)."""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    # Get the URL from command line arguments
    url = sys.argv[1]

    try:
        # Send request and read the response
        with urllib.request.urlopen(url) as response:
            # Decode and print the response body (decoded in utf-8)
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Print the error code (HTTP status code)
        print(f'Error code: {e.code}')
