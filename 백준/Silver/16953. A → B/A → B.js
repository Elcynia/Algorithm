const fs = require('fs');
const [A, B] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

function solve(A, B) {
  let cnt = 1;
  let current = B;
  while (current > A) {
    // B가 A보다 작아지면 -1 (1 ≤ A < B ≤ 10^9)
    if (current < A) return -1;

    // B가 홀수이고 1로 끝나지 않으면 -1
    if (current % 2 !== 0 && current % 10 !== 1) return -1;

    // 1로 끝나면 10으로 나눔
    if (current % 10 === 1) {
      current = Math.floor(current / 10);
    }
    // 짝수면 2로 나눔
    else if (current % 2 === 0) {
      current /= 2;
    }

    cnt++;
  }

  return current === A ? cnt : -1;
}

console.log(solve(A, B));
