#!/usr/bin/node
const { argv } = require('process');
const convertedNum = Math.floor(argv[2]);
if (!convertedNum) console.log('Missing size');
else {
  for (let i = 0; i < convertedNum; i++) {
    console.log('X'.repeat(argv[2]));
  }
}
