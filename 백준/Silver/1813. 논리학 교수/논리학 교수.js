const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const arr = input[0].split(' ').map(Number);
let answer = -1;
for (let x = 0; x <= N; x++) {
  const cnt = arr.filter((v) => v === x).length;
  if (cnt === x) {
    answer = x;
  }
}

console.log(answer);
