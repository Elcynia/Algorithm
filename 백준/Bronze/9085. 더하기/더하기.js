const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const T = +input[0];
let cnt = 1;

for (let i = 0; i < T; i++) {
  const N = +input[cnt];
  const arr = input[cnt + 1].split(' ').map(Number);
  let sum = 0;
  for (let j = 0; j < arr.length; j++) {
    sum += arr[j];
  }
  console.log(sum);
  cnt += 2;
}
