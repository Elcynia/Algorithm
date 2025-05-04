const fs = require('fs');
const [N, r, c] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

function recursion(n, r, c) {
  // 기저 조건: 크기가 1x1이 되었을 때
  if (n === 0) return 0;

  // 배열의 크기 2^n x 2^n
  const half = 1 << (n - 1); // 2^(n-1)

  // 0: 왼쪽 위, 1: 오른쪽 위, 2: 왼쪽 아래, 3: 오른쪽 아래
  if (r < half && c < half) {
    // 왼쪽 위 사분면
    return recursion(n - 1, r, c);
  } else if (r < half && c >= half) {
    // 오른쪽 위 사분면
    return half * half + recursion(n - 1, r, c - half);
  } else if (r >= half && c < half) {
    // 왼쪽 아래 사분면
    return 2 * half * half + recursion(n - 1, r - half, c);
  } else {
    // 오른쪽 아래 사분면
    return 3 * half * half + recursion(n - 1, r - half, c - half);
  }
}

console.log(recursion(N, r, c));
