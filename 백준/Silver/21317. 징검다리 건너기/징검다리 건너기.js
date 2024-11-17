const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const K = +input[N];
const jumps = input.slice(1, N).map((v) => v.split(' ').map(Number));
const dp = Array(N + 1)
  .fill()
  .map(() => [Infinity, Infinity]);

dp[1] = [0, 0];
for (let i = 2; i <= N; i++) {
  // 매우 큰 점프 미사용
  if (i - 1 >= 1) dp[i][0] = dp[i - 1][0] + jumps[i - 2][0]; // 작은 점프
  if (i - 2 >= 1) dp[i][0] = Math.min(dp[i][0], dp[i - 2][0] + jumps[i - 3][1]); // 큰 점프

  // 매우 큰 점프 사용
  if (i - 3 >= 1) dp[i][1] = dp[i - 3][0] + K; // 현재 매우 큰 점프
  if (i - 1 >= 1) dp[i][1] = Math.min(dp[i][1], dp[i - 1][1] + jumps[i - 2][0]); // 이전 사용 + 작은 점프
  if (i - 2 >= 1) dp[i][1] = Math.min(dp[i][1], dp[i - 2][1] + jumps[i - 3][1]); // 이전 사용 + 큰 점프
}

console.log(Math.min(...dp[N]));
