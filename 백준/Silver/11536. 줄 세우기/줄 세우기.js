const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const names = [];
for (let i = 1; i <= N; i++) {
  names.push(input[i].trim());
}

const cal1 = names.every((name, i) => i === 0 || names[i - 1] < name);
const cal2 = names.every((name, i) => i === 0 || names[i - 1] > name);

if (cal1) {
  console.log('INCREASING');
} else if (cal2) {
  console.log('DECREASING');
} else {
  console.log('NEITHER');
}