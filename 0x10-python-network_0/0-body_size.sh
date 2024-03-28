#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
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
