const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
let result = [];
let checked = new Array(N).fill(false);

function permutation(level) {
  if (level === N) {
    console.log(result.join(' '));
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (checked[i]) continue;
    result.push(i);
    checked[i] = true;
    permutation(level + 1);
    checked[i] = false;
    result.pop();
  }
}

permutation(0);
