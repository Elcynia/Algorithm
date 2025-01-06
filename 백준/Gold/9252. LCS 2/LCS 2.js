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

/*
?   LCS 문제에서 문자열을 추적하는 출력이 추가된 케이스.
*  시간 복잡도 : O(MN)
두 문자가 같은 경우, 문자를 lcsStr 앞에 추가한 뒤  위/왼쪽 모두 이전 위치로 이동한다 (i--, j--)
왼쪽 보다 위쪽 값이 더 큰 경우(dp[i-1][j] > dp[i][j-1]), 위쪽으로 이동한다 (i--)
위쪽 보다 왼쪽 값이 더 크거나 같은 경우 (dp[i-1][j] <= dp[i][j-1]) 왼쪽으로 이동한다 (j--)
P(6,6) → K(5,6) → A(3,5) → C(2,4) = "ACAK"
*/
