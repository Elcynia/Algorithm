const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const dp = Array(N + 1).fill(0);

for (let i = N - 1; i >= 0; i--) {
  const [T, P] = input[i].split(' ').map(Number);
  if (i + T <= N) {
    dp[i] = Math.max(P + dp[i + T], dp[i + 1]);
  } else {
    dp[i] = dp[i + 1];
  }
}

console.log(dp[0]);
