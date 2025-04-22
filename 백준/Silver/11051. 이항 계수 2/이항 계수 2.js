const fs = require('fs');
const [N, K] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

function 이항계수(n, k) {
  const dp = Array(k + 1).fill(0);
  dp[0] = 1;

  for (let i = 1; i <= n; i++) {
    for (let j = Math.min(i, k); j > 0; j--) {
      dp[j] = (dp[j] + dp[j - 1]) % 10007;
    }
  }

  return dp[k];
}

console.log(이항계수(N, K));
