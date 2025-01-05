const fs = require('fs');
const [arr1, arr2] = fs.readFileSync(0).toString().trim().split('\n');

const dp = Array.from({ length: arr1.length + 1 }, () => Array(arr2.length + 1).fill(0));

for (let i = 1; i <= arr1.length; i++) {
  for (let j = 1; j <= arr2.length; j++) {
    if (arr1[i - 1] === arr2[j - 1]) {
      dp[i][j] = dp[i - 1][j - 1] + 1;
    } else {
      dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
}
console.log(dp[arr1.length][arr2.length]);
