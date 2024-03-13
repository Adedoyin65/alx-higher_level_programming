#!/usr/bin/node
exports.logMe = (function () {
  let counter = 0; // Counter to keep track of the number of times the function has been called
  return function (item) {
    console.log(`${counter}: ${item}`);
    counter++; // Increment the counter after logging
  };
})();
