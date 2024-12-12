const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
let res = [];
for (let i = 0; i < input.length; i++) {
  res.push(+input[i]);
}
res.sort((a, b) => a - b);

console.log(res[1]);
