#!/usr/bin/node
const dict = require('./101-data.js').dict;

const keys = Object.entries(dict);
const values = Object.values(dict);
const uniqValues = [...new Set(values)];
const newDict = {};
for (const value in uniqValues) {
  const list = [];
  for (const key in keys) {
    if (keys[key][1] === uniqValues[value]) {
      list.unshift(keys[key][0]);
    }
  }
  newDict[uniqValues[value]] = list;
}
console.log(newDict);
