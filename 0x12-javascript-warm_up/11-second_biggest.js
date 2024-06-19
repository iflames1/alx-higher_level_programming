#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 3) {
  console.log(0);
} else {
  args.sort();
  console.log(args.reverse()[1]);
}
