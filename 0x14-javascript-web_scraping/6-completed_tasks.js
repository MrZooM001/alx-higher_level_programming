#!/usr/bin/node
const requrest = require('request');
const argv = process.argv;

const url = argv[2];

requrest(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const parse = JSON.parse(body);
    for (const i in parse) {
      const task = parse[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId] += 1;
        }
      }
    }
    console.log(completed);
  } else {
    console.log(response.statusCode);
  }
});
