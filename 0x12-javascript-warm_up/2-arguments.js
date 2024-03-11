#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;
if (len > 3) {
  console.log('Arguments found');
} else if (len !== 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
