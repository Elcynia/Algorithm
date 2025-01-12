const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const T = +input[0];

const dp = [0, 1, 1, 1, 2, 2];

for (let i = 6; i <= 100; i++) {
  dp[i] = dp[i - 5] + dp[i - 1];
}

for (let i = 1; i <= T; i++) {
  const N = +input[i];
  console.log(dp[N]);
}

/**
 * dp[N] = 5칸 전의 값과 1칸 전의 값의 합
 * P(6) = 3 = P(1) + P(5)
 * P(12) = 16 = P(4) + P(12)
 */
