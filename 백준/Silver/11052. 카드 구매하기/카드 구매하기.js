const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const dp = Array(N + 1).fill(0);
const arr = [0, ...input[1].split(' ').map(Number)];

for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= i; j++) {
    // i개를 구매하기 위한 카드 가격
    dp[i] = Math.max(dp[i], dp[i - j] + arr[j]);
  }
}
console.log(dp[N]);
