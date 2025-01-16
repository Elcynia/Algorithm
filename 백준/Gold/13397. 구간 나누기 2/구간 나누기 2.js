const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

let left = 0;
let right = Math.max(...arr) - Math.min(...arr);
let ans = -1;

function isPossible(k) {
  let curMin = arr[0];
  let curMax = arr[0];
  let cnt = 1;

  for (let i = 1; i < N; i++) {
    curMin = Math.min(curMin, arr[i]);
    curMax = Math.max(curMax, arr[i]);

    if (curMax - curMin > k) {
      cnt += 1;
      curMin = arr[i];
      curMax = arr[i];
    }
  }

  return cnt <= M;
}

while (left <= right) {
  const mid = Math.floor((left + right) / 2);

  if (isPossible(mid)) {
    ans = mid;
    right = mid - 1; // 가능한 값이므로 더 작은 범위 탐색
  } else {
    left = mid + 1; // 불가능하므로 더 큰 범위 탐색
  }
}

console.log(ans);
