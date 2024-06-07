#!/usr/bin/node
// Define the function
function addMeMaybe (number, theFunction) {
  number += 1; // Increment the number
  theFunction(number); // Call theFunction with the incremented number
}

// Export the function
module.exports.addMeMaybe = addMeMaybe;
