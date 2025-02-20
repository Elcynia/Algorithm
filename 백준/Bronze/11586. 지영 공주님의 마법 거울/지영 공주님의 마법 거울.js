const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const board = input.slice(1, N + 1);
const state = +input[N + 1];

const transformations = {
  1: (img) => img,
  2: (img) => img.map((row) => row.split('').reverse().join('')),
  3: (img) => img.reverse(),
};

console.log(transformations[state](board).join('\n'));
