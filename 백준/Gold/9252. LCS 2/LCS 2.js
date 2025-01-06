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

let lcsStr = '';
for (let i = arr1.length, j = arr2.length; i > 0 && j > 0; ) {
  if (arr1[i - 1] === arr2[j - 1]) {
    lcsStr = arr1[i - 1] + lcsStr;
    i--, j--;
  } else if (dp[i - 1][j] > dp[i][j - 1]) {
    i--;
  } else {
    j--;
  }
}
console.log(dp[arr1.length][arr2.length]);
console.log(lcsStr);
