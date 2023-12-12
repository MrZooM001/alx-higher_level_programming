#!/usr/bin/node
exports.converter = function (base) {
  return function (convertedNum) {
    return convertedNum.toString(base);
  };
};
