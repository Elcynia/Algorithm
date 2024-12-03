const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

let cnt = 0;
let sum = 0;
let start = 0;
let end = 0;

while (end <= N) {
  if (sum === M) {
    cnt++;
    sum -= arr[start];
    start++;
  } else if (sum < M) {
    if (end === N) break;
    sum += arr[end];
    end++;
  } else {
    sum -= arr[start];
    start++;
  }
}

console.log(cnt);
