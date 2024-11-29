const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();

const line1 = '* '.repeat(Math.ceil(N / 2));
const line2 = ' *'.repeat(Math.floor(N / 2));
for (let i = 0; i < N; i++) {
  console.log(line1);
  console.log(line2);
}
