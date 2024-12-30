const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const T = +input[0];
let cnt = 1;

for (let i = 0; i < T; i++) {
  const N = +input[cnt];
  const arr = input[cnt + 1].split(' ').map(Number);
  const sum = (N * (arr[0] + arr.at(-1))) / 2;
  console.log(sum);
  cnt += 2;
}
