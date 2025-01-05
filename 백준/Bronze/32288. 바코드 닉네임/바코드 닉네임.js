const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const arr = input[1];

let result = '';
for (let i = 0; i < N; i++) {
  const char = arr[i];
  if (char === 'l') {
    result += 'L';
  } else if (char === 'I') {
    result += 'i';
  }
}

console.log(result);
