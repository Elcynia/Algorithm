const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const arr = [0, ...input[1].split(' ').map(Number)];
let result = [];

for (let i = 1; i <= N; i++) {
  arr[i] += arr[i - 1];
}

for (let i = 2; i < M + 2; i++) {
  const [start, end] = input[i].split(' ').map(Number);
  result.push(arr[end] - arr[start - 1]);
}

console.log(result.join('\n'));
