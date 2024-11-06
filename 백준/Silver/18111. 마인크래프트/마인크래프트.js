const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M, B] = input[0].split(' ').map(Number);
const board = Array.from(input.slice(1), (v) => v.split(' ').map(Number));

let minTime = Infinity;
let optimalHeight = 0;

for (let h = 0; h <= 256; h++) {
  let time = 0;
  let inventory = B;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      const diff = board[i][j] - h; // 현재 높이와 목표 높이의 차이(diff) 계산
      if (diff > 0) {
        // 양수면
        // 블럭 제거 (2s)
        time += diff * 2;
        inventory += diff;
      } else if (diff < 0) {
        // 음수면
        // 블럭 추가 (-diff, 1s)
        time -= diff;
        inventory += diff; // 인벤에서 블럭 사용
      }
    }
  }

  if (inventory >= 0 && time <= minTime) {
    minTime = time;
    optimalHeight = h;
  }
}

console.log(minTime, optimalHeight);
