const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const S = input[1].split(' ').map(Number);
const arr = [];
const totalMoney = Array(N + M).fill(0);
for (let i = 0; i < N; i++) arr.push(input[i + 2].split(' ').map(Number));

for (let i = 0; i < N; i++) {
  totalMoney[i] = S[i];
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N + M; j++) {
    if (i !== j) {
      totalMoney[j] += arr[i][j];
      totalMoney[i] -= arr[i][j];
    }
  }
}

console.log(totalMoney.join(' '));
