const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();

const arr1 = input[0].split(' ').map(Number);
const arr2 = input[1].split(' ').map(Number);

let cnt = 0;
for (let i = 0; i < N; i++) {
  if (arr1[i] <= arr2[i]) cnt++;
}

console.log(cnt);
