#!/usr/bin/node
const requrest = require('request');
const argv = process.argv;

const url = argv[2];
const characterId = '18';
let count = 0;

requrest(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const parse = JSON.parse(body);
  parse.results.forEach(movie => {
    movie.characters.forEach(character => {
      if (character.includes(characterId)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
