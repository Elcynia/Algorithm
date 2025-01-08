const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const appMemories = [0, ...input[1].split(' ').map(Number)];
const disabledCosts = [0, ...input[2].split(' ').map(Number)];

const MAX_COST = disabledCosts.reduce((acc, cur) => acc + cur + 1, 0);
const dp = Array.from({ length: N + 1 }, () => Array(MAX_COST).fill(0));

for (let i = 1; i <= N; i++) {
  for (let cost = 0; cost < MAX_COST; cost++) {
    dp[i][cost] = dp[i - 1][cost];
    if (cost - disabledCosts[i] >= 0) {
      dp[i][cost] = Math.max(dp[i][cost], dp[i - 1][cost - disabledCosts[i]] + appMemories[i]);
    }
  }
}

let result = Infinity;
for (let cost = 0; cost < MAX_COST; cost++) {
  if (dp[N][cost] >= M) {
    result = Math.min(result, cost);
  }
}

console.log(result);
