#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
URL=$1

# Send a request to the URL and save the response body to a temporary file
RESPONSE_FILE=$(mktemp)
curl -s -o "$RESPONSE_FILE" "$URL"

# Get the size of the response body in bytes
SIZE=$(wc -c < "$RESPONSE_FILE")

# Display the size of the response body
echo "$SIZE"

# Clean up the temporary file
rm "$RESPONSE_FILE"
