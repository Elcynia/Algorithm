const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const flowers = input.map((v) => v.split(' ').map(Number));

// 3/1 -> 301, 12/31 -> 1231
function dateToInt(month, day) {
  return month * 100 + day;
}

const START_DATE = dateToInt(3, 1);
const END_DATE = dateToInt(11, 30);

const convertedFlowers = flowers.map(([startMonth, startDay, endMonth, endDay]) => [
  dateToInt(startMonth, startDay),
  dateToInt(endMonth, endDay),
]);

// 꽃이 피는 날짜 순으로 정렬, 같으면 지는 날짜가 늦은 것을 앞에 배치
convertedFlowers.sort((a, b) => {
  if (a[0] === b[0]) return b[1] - a[1]; // 같은 시작일이면 더 늦게 지는 것 먼저
  return a[0] - b[0]; // 시작일 기준 정렬
});

let answer = 0;
let currentEnd = 0; // 현재까지 선택한 꽃으로 커버되는 마지막 날짜
let idx = 0; // 현재 확인 중인 꽃의 인덱스
let maxEnd = 0; // 현재 확인 중인 꽃들 중 가장 늦게 지는 날짜

// 3월 1일 이전에 피는 꽃 중에서 가장 늦게 지는 꽃 찾기
while (idx < N && convertedFlowers[idx][0] <= START_DATE) {
  maxEnd = Math.max(maxEnd, convertedFlowers[idx][1]);
  idx++;
}

// 첫 번째 꽃 선택
if (maxEnd === 0) {
  console.log(0);
  return;
}

currentEnd = maxEnd;
answer++;

// 현재 커버되는 날짜가 11월 30일을 넘어가면 종료
while (currentEnd <= END_DATE) {
  // 현재 커버되는 날짜 이전에 피는 꽃 중에서 가장 늦게 지는 꽃 찾기
  maxEnd = 0;
  while (idx < N && convertedFlowers[idx][0] <= currentEnd) {
    maxEnd = Math.max(maxEnd, convertedFlowers[idx][1]);
    idx++;
  }

  // 더 이상 추가할 꽃이 없으면 종료
  if (maxEnd <= currentEnd) {
    console.log(0); // 모든 기간을 커버할 수 없음
    return;
  }

  // 꽃 추가
  currentEnd = maxEnd;
  answer++;

  // 11월 30일까지 커버되면 종료
  if (currentEnd > END_DATE) {
    break;
  }
}

console.log(answer);
