#!/usr/bin/node
const { argv } = require('process');
function factorial (n) {
  if (n < 0) return (-1);
  if (isNaN(n) || n === 0) return (1);
  return (n * factorial(n - 1));
}
const firstArg = Number(argv[2]);
console.log(factorial(firstArg));
