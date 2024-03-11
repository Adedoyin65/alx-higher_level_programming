#!/usr/bin/node
const { argv } = require('node:process');
let count = -1;
argv.forEach((index) => {
  count++;
});
if (count === 1) {
  console.log('No argument');
} else if (count > 1) {
  console.log(argv[count]);
}
