#!/usr/bin/node
const requrest = require('request');
const fs = require('fs');
const argv = process.argv;

const url = argv[2];
const filePath = argv[3];

requrest(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filePath, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
