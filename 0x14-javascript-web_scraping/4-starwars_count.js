#!/usr/bin/node

const request = require('request');

// Extract API URL from command line arguments
const apiUrl = process.argv[2];

// Character ID of Wedge Antilles
const characterId = '18';

// Make a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  // Parse the JSON response body
  const filmsData = JSON.parse(body);

  // Initialize count of movies with Wedge Antilles
  let moviesWithWedgeAntilles = 0;

  // Iterate over each film and check if Wedge Antilles is present
  filmsData.forEach(film => {
    // Check if characters array includes Wedge Antilles (character ID 18)
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      moviesWithWedgeAntilles++;
    }
  });

  // Print the number of movies with Wedge Antilles
  console.log(moviesWithWedgeAntilles);
});
