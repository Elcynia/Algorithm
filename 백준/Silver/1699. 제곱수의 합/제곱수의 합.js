const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
let dp = [0];
for (let i = 1; i <= N; i++) {
  dp[i] = i;
  for (let j = 1; j * j <= i; j++) {
    dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
  }
}

console.log(dp[N]);

/**
 * dp[i]: i^2의 합
 * i에서 j^2을 뺀 수(i - j*j)의 최소 제곱수 개수에 1을 더한 값과 현재 dp[i]값을 비교
 */
