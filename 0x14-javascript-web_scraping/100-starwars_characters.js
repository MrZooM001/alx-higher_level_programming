#!/usr/bin/node
const requrest = require('request');
const argv = process.argv;

const movieId = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

requrest(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const parse = JSON.parse(body);
  parse.characters.forEach(characterUrl => {
    requrest(characterUrl, (err, response, body) => {
      if (err) {
        console.log(err);
      }
      const characters = JSON.parse(body);
      console.log(characters.name);
    });
  });
});
