#!/usr/bin/node
const { dict } = require('./101-data.js');

// Compute the new dictionary
const newDict = Object.entries(dict).reduce((acc, [userId, occurrence]) => {
  // If the occurrence does not exist as a key in the accumulator, initialize it
  if (!acc[occurrence]) {
    acc[occurrence] = [];
  }
  // Push the current userId into the list for this occurrence
  acc[occurrence].push(parseInt(userId));
  return acc;
}, {});

// Print the new dictionary
console.log(newDict);
