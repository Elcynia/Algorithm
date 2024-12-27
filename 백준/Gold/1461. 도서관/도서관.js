const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const bookPositions = input[1].split(' ').map(Number);

// 양수(오른쪽 위치)와 음수(왼쪽 위치) 책들을 분리
const leftBooks = [];
const rightBooks = [];
for (const position of bookPositions) {
  if (position > 0) {
    rightBooks.push(position);
  } else {
    leftBooks.push(-position);
  }
}

// 가장 먼 책부터 처리하기 위해 내림차순 정렬
rightBooks.sort((a, b) => b - a);
leftBooks.sort((a, b) => b - a);

// M권씩 묶었을 때 가장 먼 거리만 저장
const maxDistances = [];
for (let i = 0; i < rightBooks.length; i += M) {
  maxDistances.push(rightBooks[i]);
}
for (let i = 0; i < leftBooks.length; i += M) {
  maxDistances.push(leftBooks[i]);
}

// 가장 먼 거리는 마지막에 방문하여 돌아올 필요가 없음
const totalDistance = 2 * maxDistances.reduce((sum, dist) => sum + dist, 0) - Math.max(...maxDistances);
console.log(totalDistance);
