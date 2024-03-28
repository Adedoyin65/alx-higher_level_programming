#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
URL=$1;file_1=$(mktemp);curl -s -o "$file_1" "$URL";echo "$(wc -c < "$file_1")"
