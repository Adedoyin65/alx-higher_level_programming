#!/usr/bin/node
const Square = require('./5-square.js');

class CustomSquare extends Square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = CustomSquare;
