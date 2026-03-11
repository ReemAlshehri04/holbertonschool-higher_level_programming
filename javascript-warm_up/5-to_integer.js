#!/usr/bin/node
const arg = Math.floor(Number(process.argv[2]));
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg}`);
}
