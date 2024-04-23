#!/usr/bin/node
// A script that display the status code of a GET request.
const request = require('request');

// Make a GET request to the URL
request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
