#!/usr/bin/node

const occurrences = Number(process.argv.slice(2)[0]);

if (Number.isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < occurrences) {
    console.log('C is fun');
    i++;
  }
}
