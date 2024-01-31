#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const filePath = argv[2];
const fileEncoding = 'utf8';
fs.readFile(filePath, fileEncoding, (err, data) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});
