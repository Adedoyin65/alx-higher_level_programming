#!/usr/bin/node
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  const guy = data.name;
  $('#character').text(guy);
});
