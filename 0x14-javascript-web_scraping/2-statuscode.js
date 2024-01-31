#!/usr/bin/node
const requrest = require('request');
const argv = process.argv;

const url = argv[2];
requrest(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});
