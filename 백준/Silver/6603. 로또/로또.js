const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

let arr, k;
let r = [];

function combination(idx, lev) {
  if (lev === 6) {
    console.log(r.join(' '));
    return;
  }

  for (let i = idx; i < k; i++) {
    r.push(arr[i]);
    combination(i + 1, lev + 1);
    r.pop();
  }
}

for (let i = 0; i < input.length - 1; i++) {
  [k, ...arr] = input[i].split(' ').map(Number);
  if (k === 0) return;
  combination(0, 0);
  console.log();
}
