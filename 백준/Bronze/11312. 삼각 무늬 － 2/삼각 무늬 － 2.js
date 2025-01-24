const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const T = input[0];

for (let i = 1; i <= T; i++) {
  const [A, B] = input[i].split(' ').map(Number);
  console.log((A / B) ** 2);
}
