const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
let result = [];

for (let i = 1; i <= N; i++) {
  const [x, y] = input[i].split(' ').map(Number);
  result.push([x, y]);
}

result.sort((a, b) => {
  if (a[0] === b[0]) {
    return a[1] - b[1];
  }
  return a[0] - b[0];
});
console.log(result.map((v) => v.join(' ')).join('\n'));
