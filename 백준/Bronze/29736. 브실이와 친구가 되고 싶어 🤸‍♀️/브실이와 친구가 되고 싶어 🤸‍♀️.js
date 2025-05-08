const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [A, B] = input[0].split(' ').map(Number);
const [K, X] = input[1].split(' ').map(Number);

const lower = K - X;
const upper = K + X;
let cnt = 0;

if (lower <= B && upper >= A) {
  const start = Math.max(A, lower);
  const end = Math.min(B, upper);
  cnt = end - start + 1;
}

if (cnt > 0) {
  console.log(cnt);
} else {
  console.log('IMPOSSIBLE');
}
