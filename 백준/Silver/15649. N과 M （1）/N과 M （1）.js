const fs = require('fs');
const [n, m] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

const arr = [];
const isUsed = new Array(n + 1).fill(false);
let result = '';

function func(k) {
  if (k === m) {
    result += arr.join(' ') + '\n';
    return;
  }

  for (let i = 1; i <= n; i++) {
    if (!isUsed[i]) {
      arr[k] = i;
      isUsed[i] = true;
      func(k + 1);
      isUsed[i] = false;
    }
  }
}

func(0);
console.log(result);
