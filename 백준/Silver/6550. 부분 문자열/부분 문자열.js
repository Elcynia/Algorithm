const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
let res = [];

for (let i = 0; i < input.length; i++) {
  const [s, t] = input[i].split(' ');
  let idx = 0;
  let isEquel = false;

  for (let char of t) {
    if (char === s[idx]) {
      idx++;
      if (idx === s.length) {
        isEquel = true;
        break;
      }
    }
  }

  res.push(isEquel ? 'Yes' : 'No');
}

console.log(res.join('\n'));
