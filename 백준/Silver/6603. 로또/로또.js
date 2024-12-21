const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let choose = [];
let arr, k;

function comb(idx, lev) {
  if (lev === 6) {
    console.log(choose.join(' '));
    return;
  }

  for (let i = idx; i < k; i++) {
    choose.push(arr[i]);
    comb(i + 1, lev + 1);
    choose.pop();
  }
}

let lineIndex = 0;

while (true) {
  choose = [];
  const I = input[lineIndex++].split(' ').map(Number);

  k = I[0];
  arr = I.slice(1);
  if (k === 0) {
    break;
  }

  comb(0, 0);
  console.log();
}