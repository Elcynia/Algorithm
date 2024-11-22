const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const buses = input[1].split(' ').map(Number);
const fee = [];
let total = 0;

for (let i = 2; i < N + 2; i++) {
  fee.push(input[i].split(' ').map(Number));
}

for (let i = 0; i < M - 1; i++) {
  const from = buses[i] - 1;
  const to = buses[i + 1] - 1;
  total += fee[from][to];
}

console.log(total);
