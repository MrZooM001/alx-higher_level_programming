#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const filePath = argv[2];
fs.writeFile(filePath, argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});
