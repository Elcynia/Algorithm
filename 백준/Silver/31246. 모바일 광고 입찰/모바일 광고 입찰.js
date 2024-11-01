const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
res = [];

for (let i = 1; i <= N; i++) {
  const [A, B] = input[i].split(' ').map(Number);
  const diff = B - A;
  res.push(diff);
}
res.sort((a, b) => a - b);
console.log(Math.max(0, res[K - 1]));