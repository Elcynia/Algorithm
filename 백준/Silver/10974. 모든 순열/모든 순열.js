const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
const result = new Array(N).fill(0);
const checked = new Array(N + 1).fill(false);
const answers = [];

function permutation(level) {
  if (level === N) {
    answers.push(result.join(' '));
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (!checked[i]) {
      checked[i] = true;
      result[level] = i;
      permutation(level + 1);
      checked[i] = false;
    }
  }
}

permutation(0);
console.log(answers.join('\n'));
