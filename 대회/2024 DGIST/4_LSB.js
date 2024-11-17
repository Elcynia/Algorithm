const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n').map(Number);

function getLSB(n) {
  return n & 0b1111;
}

function make4Digits(n) {
  return n.toString().padStart(4, '0');
}

function solution(digits) {
  // 2진수 변환
  const bin = digits.map((num) => {
    const lsb = getLSB(num);
    return lsb.toString(2).padStart(4, '0');
  });

  const pw = bin.join('');
  // 10진수 변환
  const result = parseInt(pw, 2);

  return make4Digits(result);
}

console.log(solution(input));
