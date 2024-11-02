const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const me = input[0];
const n = input[1];
let cnt = 0;
for (let i = 2; i < input.length; i++) {
  if (input[i] === me) cnt++;
}
console.log(cnt);