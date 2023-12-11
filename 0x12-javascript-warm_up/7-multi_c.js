#!/usr/bin/node
const { argv } = require('process');
const convertedNum = Math.floor(argv[2]);
if (!convertedNum) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < convertedNum; i++) {
    console.log('C is fun');
  }
}
