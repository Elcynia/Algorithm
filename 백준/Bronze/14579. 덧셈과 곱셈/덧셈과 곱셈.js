const fs = require('fs');
const [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
let res = 1;
for (let i = a; i <= b; i++) {
  let sum = 0;
  for (let j = 1; j <= i; j++) {
    sum += j;
  }
  res = (res * sum) % 14579;
}
console.log(res);
