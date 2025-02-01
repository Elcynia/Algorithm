const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const [N, C] = input[0].split(' ').map(Number);
const periods = input.slice(1).map(Number);
const fireworkTimes = new Set();

for (let time = 1; time <= C; time++) {
  for (let i = 0; i < N; i++) {
    // 현재 시간이 학생의 주기로 나누어 떨어지면
    if (time % periods[i] === 0) {
      fireworkTimes.add(time);
      break;
    }
  }
}

console.log(fireworkTimes.size);
