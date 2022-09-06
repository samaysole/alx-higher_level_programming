#!/usr/bin/node
const number = parseInt(process.argv[2]);
let i, j;
if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  for (i = 0; i < number; i++) {
    for (j = 0; j < number; j++) {
      console.log('X');
    }
  }
}
