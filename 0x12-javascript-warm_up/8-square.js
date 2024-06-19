#!/usr/bin/node

const occurrences = Number(process.argv.slice(2)[0]);

if (Number.isNaN(occurrences)) {
  console.log('Missing size');
} else {
  if (occurrences > 0) {
    let i = 0;
    const row = 'X'.repeat(occurrences);
    while (i < occurrences) {
      console.log(row);
      i++;
    }
  }
}
