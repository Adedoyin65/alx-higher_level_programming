#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// Add the incr method to myObject
myObject.incr = function incr () {
  this.value += 1;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
