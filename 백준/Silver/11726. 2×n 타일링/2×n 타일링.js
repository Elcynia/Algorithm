const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
const dp = new Array(N).fill(-1);
dp[0] = 1;
dp[1] = 2;

for (let i = 2; i < N; i++) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
}

console.log(dp[N - 1]);
