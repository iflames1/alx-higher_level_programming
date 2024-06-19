#!/usr/bin/node

const args = process.argv.slice(2);

const number = Number(args[0]);

if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
