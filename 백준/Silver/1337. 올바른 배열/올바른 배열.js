const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = parseInt(input[0]);
const arr = input
  .slice(1)
  .map(Number)
  .sort((a, b) => a - b);
let mx = 4;
for (let left = 0; left < n; left++) {
  let right = left;
  while (right < n && arr[right] - arr[left] < 5) {
    right++;
  }
  let count = right - left;
  mx = Math.min(mx, 5 - count);
}

console.log(mx);
