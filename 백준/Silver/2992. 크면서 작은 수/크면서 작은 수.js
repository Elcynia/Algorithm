const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();

let digits = input.split('').map(Number);
let i = digits.length - 2;

// 오른쪽에서 왼쪽으로 탐색하며 오름차순이 깨지는 지점 찾기
while (i >= 0 && digits[i] >= digits[i + 1]) i--;

if (i === -1) {
  console.log(0);
} else {
  // i 위치의 숫자보다 큰 수 중 가장 작은 수를 i 오른쪽에서 찾기
  let j = digits.length - 1;
  while (digits[j] <= digits[i]) j--;

  // i <-> j swap
  [digits[i], digits[j]] = [digits[j], digits[i]];

  // i 오른쪽 숫자 오름차순 정렬
  let right = digits.slice(i + 1).sort((a, b) => a - b);
  digits = [...digits.slice(0, i + 1), ...right];

  console.log(parseInt(digits.join('')));
}
