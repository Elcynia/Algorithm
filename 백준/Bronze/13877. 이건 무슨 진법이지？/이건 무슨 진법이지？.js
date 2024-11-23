const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];

for (let i = 1; i <= N; i++) {
  const [idx, number] = input[i].split(' ').map(Number);
  const oct = /^[0-7]+$/.test(number) ? parseInt(number, 8) : 0;
  console.log(idx, oct, number, parseInt(number, 16));
}
