const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const dp = Array(N).fill(1);
const arr = input.map((v) => v.split(' ').map(Number));
arr.sort((a, b) => a[0] - b[0]);

for (let i = 0; i < N; i++) {
  for (let j = 0; j < i; j++) {
    // B 전봇대 번호가 증가하는 경우에만
    if (arr[j][1] < arr[i][1]) {
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
}

const mx = Math.max(...dp);

console.log(N - mx);
