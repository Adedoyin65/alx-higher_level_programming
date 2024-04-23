#!/usr/bin/node
const request = require('request');

function countWedgeAntillesMovies (apiUrl) {
  request({ url: apiUrl, json: true }, (error, response) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }

    const films = response.body.results;
    const wedgeMoviesCount = films.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ).length;

    console.log(`${wedgeMoviesCount}`);
  });
}

const apiUrl = process.argv[2];
if (!apiUrl) {
  console.error('Usage: node script.js <API_URL>');
  process.exit(1);
}

countWedgeAntillesMovies(apiUrl);
