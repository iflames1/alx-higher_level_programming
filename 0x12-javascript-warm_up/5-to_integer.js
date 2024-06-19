#!/usr/bin/node

const args = process.argv.slice(2);

let number = Number(args[0]);

if (typeof number === "number") {
  console.log(`My number: ${number}`);
} else {
  console.log("Not a number");
}
