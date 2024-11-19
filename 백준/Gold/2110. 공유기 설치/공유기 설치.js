const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, C] = input[0].split(' ').map(Number); // 집 개수, 공유기 개수
const x = input
  .slice(1)
  .map(Number)
  .sort((a, b) => a - b);
let left = 1;
let right = x[N - 1] - x[0];
let result = 0;

function wireless(dist) {
  let cnt = 1;
  let lastPosition = x[0];

  for (let i = 1; i < N; i++) {
    if (x[i] - lastPosition >= dist) {
      cnt++;
      lastPosition = x[i];
      if (cnt >= C) return true;
    }
  }

  return false;
}

while (left <= right) {
  const mid = Math.floor((left + right) / 2);

  if (wireless(mid)) {
    result = mid;
    left = mid + 1;
  } else {
    right = mid - 1;
  }
}

console.log(result);
