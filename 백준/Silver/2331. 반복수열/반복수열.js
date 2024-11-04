const fs = require('fs');
const [A, P] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
let res = [A];

function nextNumber(num, power) {
  const digits = num.toString().split('');
  let sum = 0;
  for (let i = 0; i < digits.length; i++) {
    sum += Math.pow(Number(digits[i]), power);
  }
  return sum;
}

// 반복되는 숫자 탐색
while (1) {
  const next = nextNumber(res[res.length - 1], P);
  if (res.includes(next)) break; // 중복이 발생하면 종료
  res.push(next); // 중복이 없다면 배열에 추가
}

const index = res.indexOf(nextNumber(res[res.length - 1], P));
console.log(index);
