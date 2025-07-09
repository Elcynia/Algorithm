const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = input.shift();

let result = [];

for (let i = 0; i < N; i++) {
  const [a, d, g] = input[i].split(' ').map(Number);
  if (a === d + g) {
    result.push(a * (d + g) * 2);
  } else {
    result.push(a * (d + g));
  }
}

console.log(Math.max(...result));
