const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const times = input.slice(1).map(Number);

let time = 30;
let cnt = 0;

for (let i = 0; i < N; i++) {
  const chapter = times[i];
  if (time >= chapter) {
    cnt++;
    time -= chapter;
  } else {
    if (time * 2 >= chapter) {
      cnt++;
    }
    // 다음 30분 시작
    time = 30;
  }

  // 남은 시간이 0이 되면 다음 30분 시작
  if (time === 0) {
    time = 30;
  }
}

console.log(cnt);