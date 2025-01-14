const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, H] = input[0].split(' ').map(Number);
const tops = [];
const bottoms = [];

function getIdx(arr, num) {
  let cur = -1;
  let end = arr.length;

  while (end !== 0) {
    while (cur + end < arr.length && arr[cur + end] <= num) {
      cur += end;
    }
    end = Math.floor(end / 2);
  }

  return cur;
}

for (let i = 1; i <= N; i++) {
  const num = +input[i];
  if (i % 2 === 0) {
    bottoms.push(num);
  } else {
    tops.push(H - num + 1);
  }
}

tops.sort((a, b) => a - b);
bottoms.sort((a, b) => a - b);

let min = Infinity;
let minNum = 0;

for (let h = 1; h <= H; h++) {
  const cntBot = Math.floor(N / 2) - (getIdx(bottoms, h - 1) + 1);
  const cntTop = getIdx(tops, h) + 1;

  if (min === cntBot + cntTop) {
    minNum++;
  }

  if (min > cntBot + cntTop) {
    min = cntBot + cntTop;
    minNum = 1;
  }
}

console.log(`${min} ${minNum}`);
