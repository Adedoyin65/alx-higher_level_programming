#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

// Extract movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL with the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Extract and print the movie title
  console.log(movieData.title);
});
