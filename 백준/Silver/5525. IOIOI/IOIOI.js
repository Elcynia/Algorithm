const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const [S, M] = input.slice(1);
let cnt = 0;
let patternCnt = 0;

for (let i = 1; i < M.length - 1; i++) {
  if (M[i - 1] === 'I' && M[i] === 'O' && M[i + 1] === 'I') {
    patternCnt++;
    if (patternCnt === N) {
      cnt++;
      patternCnt--;
    }
    i++;
  } else {
    patternCnt = 0;
  }
}

console.log(cnt);
