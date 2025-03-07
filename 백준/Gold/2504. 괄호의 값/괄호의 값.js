const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('');

function solution(input) {
  const S = [];

  for (let i = 0; i < input.length; i++) {
    const cur = input[i];

    if (cur === '(' || cur === '[') {
      S.push(cur);
    } else if (cur === ')' || cur === ']') {
      if (S.length === 0) return 0;

      const value = cur === ')' ? 2 : 3;
      const openBracket = cur === ')' ? '(' : '[';

      if (S[S.length - 1] === openBracket) {
        S.pop();
        S.push(value);
      } else {
        // 괄호 사이에 값들이 있는 경우
        let temp = 0;
        while (S.length > 0 && typeof S[S.length - 1] === 'number') {
          temp += S.pop();
        }

        if (S.length === 0 || S[S.length - 1] !== openBracket) {
          return 0;
        }

        S.pop();
        S.push(temp * value);
      }
    }
  }

  // 모든 처리 후 스택에 숫자만 남아있는지 확인하고 합계 계산
  let result = 0;
  for (const item of S) {
    if (typeof item !== 'number') return 0;
    result += item;
  }

  return result;
}

console.log(solution(input));
