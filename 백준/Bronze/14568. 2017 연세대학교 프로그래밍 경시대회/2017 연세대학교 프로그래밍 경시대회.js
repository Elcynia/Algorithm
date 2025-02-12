const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();

let count = 0;

// 택희(t), 영훈(y), 남규(n)
for (let t = 2; t <= N; t += 2) {
  for (let y = 1; y <= N - t; y++) {
    let n = N - t - y;
    if (n > y + 1 && n >= 1) {
      count++;
    }
  }
}

console.log(count);
