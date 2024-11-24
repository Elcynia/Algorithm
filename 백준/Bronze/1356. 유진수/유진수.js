const fs = require('fs');
const N = fs.readFileSync(0).toString().trim();

function isYujinNumber(N) {
  for (let i = 1; i < N.length; i++) {
    const front = N.slice(0, i);
    const back = N.slice(i);

    // 자리수 곱 계산
    const a = [...front].reduce((acc, cur) => acc * Number(cur), 1);
    const b = [...back].reduce((acc, cur) => acc * Number(cur), 1);

    // 유진수 판별
    if (a === b) {
      return true;
    }
  }

  return false;
}

if (isYujinNumber(N)) {
  console.log('YES');
} else {
  console.log('NO');
}
