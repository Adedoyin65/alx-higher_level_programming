#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers greater than 0
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If the conditions are not met, create an "empty" object
      // This is effectively done by not setting the width and height properties
    }
  }

  print () {
    if (this.width && this.height) {
      // Loop through each row
      for (let row = 0; row < this.height; row++) {
        // Repeat the X character width times and print it
        console.log('X'.repeat(this.width));
      }
    } else {
      console.log('Rectangle dimensions are not set.');
    }
  }
}
module.exports = Rectangle;
