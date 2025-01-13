const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
const dp = new Array(N + 1).fill(0);
dp[1] = dp[4] = 1;
dp[2] = 2;
dp[3] = 3;

for (let i = 5; i <= N; i++) {
  dp[i] = i;
  for (let j = 1; j * j <= i; j++) {
    dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
  }
}

console.log(dp[N]);
