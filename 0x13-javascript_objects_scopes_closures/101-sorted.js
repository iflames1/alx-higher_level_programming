#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}

console.log(newDict);
