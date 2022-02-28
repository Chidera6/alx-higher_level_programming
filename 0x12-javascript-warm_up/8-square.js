#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (Number(x) !== true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X');
  }
}
