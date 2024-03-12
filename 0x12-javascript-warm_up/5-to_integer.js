#!/usr/bin/node
const [arg1] = process.argv.slice(2);
const number = parseInt(arg1);
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
