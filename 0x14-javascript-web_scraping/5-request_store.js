#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Extract URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Write the response body to the specified file
  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (writeError) => {
    if (writeError) {
      console.error('Error writing to file:', writeError);
      process.exit(1);
    }
  });
});
