const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const arr = [0, ...input[1].split(' ').map(Number)];
const questionN = +input[2];
const questions = [];

for (let i = 3; i < questionN + 3; i++) {
  questions.push(input[i].split(' ').map(Number));
}

const dp = Array.from({ length: N + 1 }, () => Array(N + 1).fill(0));

// 길이가 1인 경우 (펠린드롬)
for (let i = 1; i <= N; i++) {
  dp[i][i] = 1;
}

// 길이가 2인 경우 (펠린드롬)
for (let i = 1; i < N; i++) {
  if (arr[i] === arr[i + 1]) {
    dp[i][i + 1] = 1;
  }
}

for (let i = 3; i <= N; i++) {
  for (let j = 1; j <= N - i + 1; j++) {
    const end = j + i - 1; // 끝 인덱스
    if (arr[j] === arr[end] && dp[j + 1][end - 1]) {
      dp[j][end] = 1;
    }
  }
}

let answer = '';
for (let i = 3; i < questionN + 3; i++) {
  const [S, E] = input[i].split(' ').map(Number);
  answer += dp[S][E] + '\n';
}
console.log(answer.trim());

/**
 *! 단순 계산 시 시간 복잡도는 O(NM)으로, 시간 초과 발생
 ** (N = 2,000 일 때, NM은 2,000,000,000 (20억) 이므로 시간 범위 내에 처리 불가)
 *? dp를 이용하면 시간 복잡도는 O(N^2)으로 줄일 수 있으므로 dp를 이용해 풀어야 함.
 ** (N = 2,000 일 때, N^2은 4,000,000 (400만) 이므로 시간 범위 내에 처리 가능, O(N^2 + M))
 i번째부터 j번쨰까지 팰린드롬이면 dp[i][j] = 1
 구간의 길이가 1인 경우는 무조건 하나뿐이므로, 펠린드롬 처리 (1)
 구간의 길이가 2일 때, 두 수가 같으면 펠린드롬 처리 (1)
 */
