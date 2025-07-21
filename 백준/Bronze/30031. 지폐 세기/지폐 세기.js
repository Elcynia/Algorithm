const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();

const money = {
  136: 1000,
  142: 5000,
  148: 10000,
  154: 50000,
};

let sum = 0;
for (let i = 0; i < N; i++) {
  const [r, c] = input[i].split(' ').map(Number);
  if (money[r]) {
    sum += money[r];
  }
}
console.log(sum);
