const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [L, C] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').sort();
const words = ['a', 'e', 'i', 'o', 'u'];
let result = [];

function isValid() {
  let vCnt = 0;
  for (let word of result) {
    if (words.includes(word)) {
      vCnt++;
    }
  }
  const conCnt = L - vCnt; // 자음 수 계산
  return vCnt >= 1 && conCnt >= 2; // 모음1, 자음2 체크
}

function comb(idx, lev) {
  if (lev === L) {
    if (isValid()) {
      console.log(result.join(''));
    }
    return;
  }

  for (let i = idx; i < C; i++) {
    result.push(arr[i]);
    comb(i + 1, lev + 1);
    result.pop();
  }
}

comb(0, 0);
