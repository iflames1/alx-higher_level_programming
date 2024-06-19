#!/usr/bin/node

const args = process.argv.slice(2);

const first = Number(args[0]);
const second = Number(args[1]);

function add (a, b) {
  console.log(a + b);
}

add(first, second);
