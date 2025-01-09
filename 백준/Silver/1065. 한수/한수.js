const fs = require('fs');
const N = fs.readFileSync(0).toString().trim();

function isHansu(num) {
  if (num < 100) return true;
  const digits = String(num).split('').map(Number);
  const diff = digits[1] - digits[0];
  for (let i = 1; i < digits.length - 1; i++) {
    if (digits[i + 1] - digits[i] !== diff) return false;
  }
  return true;
}

let cnt = 0;
for (let i = 1; i <= N; i++) {
  if (isHansu(i)) cnt++;
}

console.log(cnt);

/*
한 자릿수, 두 자릿 수는 모두 한수임이 자명하므로 무조건 true (1 ~ 9, 10 ~ 99)
두 자릿수가 넘어간다면 숫자 자릿수 분리
첫 두 자릿수의 차이를 기준으로 나머지 자릿수가 동일한 차이면 true
*/
