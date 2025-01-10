const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
const bookCnt = {};

for (let i = 1; i <= N; i++) {
  const book = input[i];
  if (bookCnt[book]) bookCnt[book]++;
  else bookCnt[book] = 1;
}

const maxCnt = Math.max(...Object.values(bookCnt));
const result = Object.keys(bookCnt).filter((book) => bookCnt[book] === maxCnt);
console.log(result.sort()[0]);

/**
 * 책이 등장할 때마다 해당 책의 카운트 +1 증가
 * 가장 많이 등장한 책 제목을 maxCnt에 저장
 * 사전 순으로 정렬하여 가장 앞에 있는 제목 출력
 *
 */
