const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, X] = input[0].split(' ').map(Number);
let ans = -1;

for (let i = 0; i < N; i++) {
  const [S, T] = input[i + 1].split(' ').map(Number);
  if (S + T <= X && ans < S) {
    ans = S;
  }
}

console.log(ans);
