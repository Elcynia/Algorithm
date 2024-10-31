const fs = require('fs');

function solution(s) {
  let prevS = '';
  while (prevS !== s) {
    prevS = s;
    s = s.replace(/\(\)/g, '(1)');
    s = s.replace(/\)\(/g, ')+(');
  }
  return s;
}

const input = fs.readFileSync('/dev/stdin').toString().trim();
console.log(solution(input));