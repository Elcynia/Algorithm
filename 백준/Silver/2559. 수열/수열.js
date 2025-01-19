const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

let sum = 0;

for (let i = 0; i < K; i++) {
  sum += arr[i];
}

let maxSum = sum;

for (let i = K; i < N; i++) {
  sum = sum + arr[i] - arr[i - K];
  maxSum = Math.max(maxSum, sum);
}

console.log(maxSum);

/**
 * 슬라이딩 윈도우 이용
 * 윈도우를 한 칸씩 오른쪽으로 밀면서 새로운 값 추가 (arr[i]) 및 제일 왼쪽 값 제거 (arr[i-K])
 */
