const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, S, M] = input[0].split(' ').map(Number); // 곡의 개수, 시작 볼륨, 최대 볼륨
const V = input[1].split(' ').map(Number);
let dp = Array.from(Array(N + 1), () => new Array(M + 1).fill(false));
let result = -1;
dp[0][S] = true; // 시작 볼륨 S에서 시작

for (let i = 1; i <= N; i++) {
  for (let j = 0; j <= M; j++) {
    if (dp[i - 1][j]) {
      if (j + V[i - 1] <= M) dp[i][j + V[i - 1]] = true;
      if (j - V[i - 1] >= 0) dp[i][j - V[i - 1]] = true;
    }
  }
}

for (let j = M; j >= 0; j--) {
  if (dp[N][j]) {
    result = j;
    break;
  }
}
console.log(result);