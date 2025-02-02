const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const T = +input[0];
let cur = 1;

function solution(commands, arr) {
  let head = 0;
  let tail = arr.length;
  let isReversed = false;

  for (const cmd of commands) {
    if (cmd === 'R') {
      isReversed = !isReversed;
    } else if (cmd === 'D') {
      if (head >= tail) return 'error';
      isReversed ? tail-- : head++;
    }
  }

  const result = arr.slice(head, tail);
  return `[${isReversed ? result.reverse() : result}]`;
}

for (let t = 0; t < T; t++) {
  const commands = input[cur++];
  const n = +input[cur++];
  const arr = input[cur++]
    .slice(1, -1)
    .split(',')
    .filter((x) => x !== '')
    .map(Number);

  console.log(solution(commands, arr));
}
