const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const arr = input[1].split(' ').map(Number);

const dp = new Array(N);
dp[0] = arr[0];

for (let i = 1; i < N; i++) {
  dp[i] = Math.max(arr[i], dp[i - 1] + arr[i]);
}

console.log(Math.max(...dp));