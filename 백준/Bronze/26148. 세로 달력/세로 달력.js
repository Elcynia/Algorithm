const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const year = +input[0];
let monthStart = +input[1];

// 윤년 여부 판단 (400의 배수이거나, 4의 배수이면서 100의 배수가 아니면 윤년)
const isLeap = year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0);

// 각 월의 일수 (2월은 윤년이면 29, 아니면 28)
const monthDays = [31, isLeap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

let totalVerticalCalendars = 0;

// 12개월에 대해 계산
for (let m = 0; m < 12; m++) {
  const D = monthDays[m]; // m월의 일수

  // 각 요일(1~7)에 대해 해당 월에 몇 개의 날짜가 찍히는지 계산
  for (let w = 1; w <= 7; w++) {
    // m월의 시작 요일(monthStart)부터 해당 요일 w가 처음 등장하는 날짜 구하기
    // 만약 w가 monthStart보다 크거나 같으면, 첫 등장 날짜는 (w - monthStart + 1)
    // 아니라면, 다음 주에 등장하므로 (7 - monthStart + 1) + w
    let firstOccurrence;
    if (w >= monthStart) firstOccurrence = w - monthStart + 1;
    else firstOccurrence = 7 - monthStart + 1 + w;

    // 만약 첫 등장 날짜가 m월의 마지막 날짜보다 크다면, 그 열에는 날짜가 없음
    if (firstOccurrence > D) continue;

    // 해당 열에 몇 개의 날짜가 있는지 계산
    // 첫 등장 날짜부터 7일 간격으로 들어감
    const count = 1 + Math.floor((D - firstOccurrence) / 7);

    // 만약 해당 열에 정확히 5개의 날짜가 있다면 "세로 달력"에 해당
    if (count === 5) totalVerticalCalendars++;
  }

  // 다음 월의 시작 요일 업데이트
  // 한 달의 남은 일수를 7로 나눈 나머지만큼 요일이 이동한다.
  monthStart = (monthStart + (D % 7)) % 7;
  if (monthStart === 0) monthStart = 7; // 0이 나오면 7(토요일)로 맞춤
}

console.log(totalVerticalCalendars);
