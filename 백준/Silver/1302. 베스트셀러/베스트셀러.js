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
