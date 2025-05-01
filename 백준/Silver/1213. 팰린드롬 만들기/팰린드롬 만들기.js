const fs = require('fs');
const str = fs.readFileSync(0).toString().trim().split('');

const charCount = {};

for (let i = 0; i < str.length; i++) {
  const char = str[i];
  if (charCount[char]) {
    charCount[char]++;
  } else {
    charCount[char] = 1;
  }
}

// 홀수 개수
let oddCount = 0;
let oddChar = '';
for (const char in charCount) {
  if (charCount[char] % 2 !== 0) {
    oddCount++;
    oddChar = char;
  }
}

// 홀수 2개 이상
if (oddCount > 1) {
  console.log("I'm Sorry Hansoo");
} else {
  let result = [];
  const sortedChars = Object.keys(charCount).sort();
  // 앞에서부터 절반씩 배치
  for (const char of sortedChars) {
    const count = Math.floor(charCount[char] / 2);
    for (let i = 0; i < count; i++) {
      result.push(char);
    }
  }
  // 홀수 개수의 문자가 있으면 중앙에 배치
  if (oddChar) {
    result.push(oddChar);
  }
  // 나머지 절반은 역순으로 배치
  for (let i = result.length - 1 - (oddChar ? 1 : 0); i >= 0; i--) {
    result.push(result[i]);
  }

  console.log(result.join(''));
}
