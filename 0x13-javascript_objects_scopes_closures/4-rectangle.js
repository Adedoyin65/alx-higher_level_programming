#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // If w or h is not a positive integer or is equal to 0,
    // this instance effectively becomes an "empty" object by not setting width and height.
  }

  print () {
    if (this.width && this.height) {
      // Print the rectangle using the character X
      for (let row = 0; row < this.height; row++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      console.log('Rectangle dimensions are not set.');
    }
  }

  rotate () {
    if (this.width && this.height) {
      // Swap width and height
      [this.width, this.height] = [this.height, this.width];
    } else {
      console.log('Rectangle dimensions are not set, cannot rotate.');
    }
  }

  double () {
    if (this.width && this.height) {
      // Double the width and height
      this.width *= 2;
      this.height *= 2;
    } else {
      console.log('Rectangle dimensions are not set, cannot double.');
    }
  }
}
module.exports = Rectangle;
