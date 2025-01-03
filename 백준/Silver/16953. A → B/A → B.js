const fs = require('fs');
const [A, B] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

const Q = [[A, 0]]; // [현재 숫자, 연산 횟수]
const visited = new Set([A]);

while (Q.length) {
  const [num, cnt] = Q.shift();
  if (num === B) {
    console.log(cnt + 1);
    return;
  }

  // 2를 곱하는 경우
  if (num * 2 <= B && !visited.has(num * 2)) {
    Q.push([num * 2, cnt + 1]);
    visited.add(num * 2);
  }

  // 1을 오른쪽에 추가하는 경우
  const addNumber = num * 10 + 1;
  if (addNumber <= B && !visited.has(addNumber)) {
    Q.push([addNumber, cnt + 1]);
    visited.add(addNumber);
  }
}

console.log(-1);
