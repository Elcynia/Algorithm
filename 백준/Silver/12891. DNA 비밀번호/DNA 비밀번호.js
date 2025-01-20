const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [S, P] = input[0].split(' ').map(Number);
const arr = input[1];
const [A, C, G, T] = input[2].split(' ').map(Number);

let cnt = 0;
let cntDNA = { A: 0, C: 0, G: 0, T: 0 };

// ACGT 개수 카운트
for (let i = 0; i < P; i++) {
  cntDNA[arr[i]]++;
}

if (cntDNA['A'] >= A && cntDNA['C'] >= C && cntDNA['G'] >= G && cntDNA['T'] >= T) {
  cnt++;
}

// 슬라이딩 윈도우
for (let i = P; i < S; i++) {
  const removed = arr[i - P];
  const added = arr[i];

  cntDNA[removed]--; // 왼쪽 문자 제거
  cntDNA[added]++; // 오른쪽 문자 추가

  if (cntDNA['A'] >= A && cntDNA['C'] >= C && cntDNA['G'] >= G && cntDNA['T'] >= T) {
    cnt++;
  }
}

console.log(cnt);
