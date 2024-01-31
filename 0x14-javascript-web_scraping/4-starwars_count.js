#!/usr/bin/node
const requrest = require('request');
const argv = process.argv;

const url = argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

requrest(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const parse = JSON.parse(body);
  parse.results.forEach(movie => {
    if (movie.characters.includes(characterUrl)) {
      count++;
    }
  });
  console.log(count);
});
