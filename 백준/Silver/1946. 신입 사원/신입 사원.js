const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const T = +input.shift();
let line = 0;

for (let t = 0; t < T; t++) {
  const N = +input[line++];

  const people = [];
  for (let i = 0; i < N; i++) {
    const [paperScore, interviewScore] = input[line++].split(' ').map(Number);
    people.push({ paperScore, interviewScore });
  }

  people.sort((a, b) => a.paperScore - b.paperScore);

  let cnt = 0;
  let rank = Infinity;

  for (let i = 0; i < N; i++) {
    // 현재까지 본 지원자 중에서 면접 순위가 가장 높으면 선발
    if (people[i].interviewScore < rank) {
      rank = people[i].interviewScore;
      cnt++;
    }
  }

  console.log(cnt);
}
