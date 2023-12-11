#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 3 || argv.length === 3) console.log(0);
else {
  const argsArr = argv.splice(2, argv.length).map(Number);
  const secondBig = argsArr.sort(function (x, y) { return y - x; })[1];
  console.log(secondBig);
}
