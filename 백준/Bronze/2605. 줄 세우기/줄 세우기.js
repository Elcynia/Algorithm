const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const numbers = input[1].split(' ').map(Number);
const res = [];

for (let i = 0; i < n; i++) {
  const tmp = i - numbers[i];
  res.splice(tmp, 0, i + 1);
}

console.log(res.join(' '));