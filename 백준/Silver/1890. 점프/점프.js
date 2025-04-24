const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const arr = input.map((v) => v.split(' ').map(Number));
const dp = Array.from({ length: N }, () => Array(N).fill(0n));

dp[0][0] = 1n;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (dp[i][j] === 0n || (i === N - 1 && j === N - 1)) continue;

    const jump = arr[i][j];
    if (jump === 0) continue;

    // 오른쪽으로 점프
    if (j + jump < N) {
      dp[i][j + jump] += dp[i][j];
    }

    // 아래쪽으로 점프
    if (i + jump < N) {
      dp[i + jump][j] += dp[i][j];
    }
  }
}

console.log(dp[N - 1][N - 1].toString());
