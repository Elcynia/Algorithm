const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, S] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
let ans = 0;

function search(lev, sum) {
  if (lev === N) {
    if (sum === S) ans++;
    return;
  }

  // 인덱스가 lev인 원소 선택 O
  search(lev + 1, sum + arr[lev]);

  // 인덱스가 lev인 원소 선택 X
  search(lev + 1, sum);
}

search(0, 0);
console.log(S === 0 ? ans - 1 : ans); // 공집합을 제외하기 위해 S가 0이면 1을 뺌
