const fs = require('fs');
const n = +fs.readFileSync(0).toString().trim();
let cnt = 0;

for (let i = 1; i <= n; i++) {
  if (String(i).includes('50')) {
    cnt += 2;
  } else {
    cnt += 1;
  }
}

if (String(n).includes('50')) {
  cnt -= 1;
}

console.log(cnt);
