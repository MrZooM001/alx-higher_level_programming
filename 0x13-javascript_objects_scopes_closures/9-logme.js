#!/usr/bin/node
exports.logMe = function (item) {
  this.item = item;
  this.instanceCount = (this.instanceCount || 0);
  console.log(`${this.instanceCount++}: ${this.item}`);
};
