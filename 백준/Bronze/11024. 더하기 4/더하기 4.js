const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
for (let i = 1; i <= N; i++) {
  console.log(
    input[i]
      .split(' ')
      .map(Number)
      .reduce((acc, cur) => acc + cur)
  );
}
