#!/usr/bin/node
const requrest = require('request');
const argv = process.argv;

const filmId = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

requrest(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const parse = JSON.parse(body);
  console.log(parse.title);
});
