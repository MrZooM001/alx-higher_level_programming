#!/usr/bin/node
const { argv } = require('process');
const convertedNum = Math.floor(argv[2]);
if (!convertedNum) console.log('Not a number');
else console.log('My number:', convertedNum);
