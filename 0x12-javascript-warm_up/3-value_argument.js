#!/usr/bin/node
const [dan] = process.argv.slice(2);
if (dan === undefined) {
  console.log('No argument');
} else {
  console.log(dan);
}
