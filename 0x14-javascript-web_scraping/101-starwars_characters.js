#!/usr/bin/node
const requrest = require('request');
const argv = process.argv;

const movieId = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

requrest(url, (err, response, body) => {
  if (!err) {
    const parse = JSON.parse(body);
    const characters = parse.characters;
    printNames(characters, 0);
  }
});

function printNames (characterUrl, index) {
  requrest(characterUrl[index], (err, response, body) => {
    if (!err) {
      const character = JSON.parse(body);
      console.log(character.name);
      if (index + 1 < characterUrl.length) {
        printNames(characterUrl, index + 1);
      }
    }
  });
}
