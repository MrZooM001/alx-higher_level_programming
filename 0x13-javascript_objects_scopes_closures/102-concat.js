#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');
const fileA = fs.readFileSync(argv[2].toString());
const fileB = fs.readFileSync(argv[3].toString());
const fileC = fileA + fileB;
fs.writeFileSync(argv[4], fileC);
