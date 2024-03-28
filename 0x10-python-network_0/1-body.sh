#!/bin/bash
# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
URL=$1

# Send a GET request to the URL and save the response headers to a temporary file
HEADERS_FILE=$(mktemp)
curl -s -D "$HEADERS_FILE" -o /dev/null "$URL"

# Get the response status code from the headers file
STATUS_CODE=$(awk NR==1{print } "$HEADERS_FILE")

# Check if the status code is 200
if [ "$STATUS_CODE" -eq 200 ]; then
  # Send a GET request again to get the response body and display it
  curl -s "$URL"
else
  echo "Error: Non-200 status code received - $STATUS_CODE"
fi

# Clean up the temporary files
rm "$HEADERS_FILE"
