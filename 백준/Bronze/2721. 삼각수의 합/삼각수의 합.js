const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n').map(Number);
const TC = input[0];

for (let i = 1; i <= TC; i++) {
  const n = input[i];
  let result = 0;
  for (let k = 1; k <= n; k++) {
    // k * T(k+1)
    // T(k+1)은 1부터 (k+1)까지의 합 = (k+1)(k+2)/2
    let cal = ((k + 1) * (k + 2)) / 2;
    result += k * cal;
  }

  console.log(result);
}
