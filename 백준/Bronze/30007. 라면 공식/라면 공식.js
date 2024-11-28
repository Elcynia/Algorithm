const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = +input[0];

for (let i = 1; i <= n; i++) {
  const [A, B, X] = input[i].split(' ').map(Number);
  console.log(A * (X - 1) + B);
}
