const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const arr_A = input[1].split(' ').map(Number);
const arr_B = input[2].split(' ').map(Number);
let result = 0;

arr_A.sort((a, b) => a - b);
arr_B.sort((a, b) => b - a);

for (let i = 0; i < N; i++) {
  result += arr_A[i] * arr_B[i];
}
console.log(result);
