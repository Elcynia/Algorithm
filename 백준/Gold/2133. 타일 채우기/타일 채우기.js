const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
const dp = new Array(N + 1).fill(0);

if (N % 2 !== 0) {
  console.log(0);
  return;
}

dp[0] = 1;
dp[2] = 3;

for (let i = 4; i <= N; i += 2) {
  dp[i] = dp[i - 2] * 3;
  for (let j = i - 4; j >= 0; j -= 2) {
    dp[i] += dp[j] * 2;
  }
}
console.log(dp[N]);

/**
 * 빈 타일을 채우는 경우
 * 3*2 타일을 채우는 경우
 */
