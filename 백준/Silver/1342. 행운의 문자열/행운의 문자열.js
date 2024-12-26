const fs = require('fs');
const S = fs.readFileSync(0).toString().trim().split('');
let ans = 0;
const used = new Array(S.length).fill(false);

function search(prev, depth) {
  if (depth === S.length) {
    ans++;
    return;
  }

  let checked = new Set();
  for (let i = 0; i < S.length; i++) {
    if (!used[i] && !checked.has(S[i]) && S[i] !== prev) {
      used[i] = true;
      checked.add(S[i]);
      search(S[i], depth + 1);
      used[i] = false;
    }
  }
}

search('', 0);
console.log(ans);
