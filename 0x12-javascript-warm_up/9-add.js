#!/usr/bin/node
const { argv } = require('process');
function add (a, b) {
  return (a + b);
}
const firstNum = Math.floor(argv[2]);
const secondNum = Math.floor(argv[3]);
if (!firstNum && !secondNum) console.log(NaN);
else {
  console.log(add(firstNum, secondNum));
}
