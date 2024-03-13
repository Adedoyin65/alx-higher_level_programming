#!/usr/bin/node
exports.converter = function (base) {
  return function convertNumber (num) {
    if (num < base) {
      return num.toString(base);
    } else {
      return convertNumber(Math.floor(num / base)) + (num % base).toString(base);
    }
  };
};
