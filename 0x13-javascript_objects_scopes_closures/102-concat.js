#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (fileA && fileB && fileC) {
  const dataA = fs.readFileSync(fileA, 'utf8');
  const dataB = fs.readFileSync(fileB, 'utf8');
  fs.writeFileSync(fileC, dataA + dataB);
} else {
  console.log('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
}
