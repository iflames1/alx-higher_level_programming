#!/usr/bin/node

const occurrences = Number(process.argv[2]);

if (Number.isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < occurrences) {
    console.log('C is fun');
    i++;
  }
}
