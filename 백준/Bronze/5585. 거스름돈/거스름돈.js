const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
const coins = [500, 100, 50, 10, 5, 1];
let money = 1000 - N;
let result = 0;
for (let i of coins) {
  result += parseInt(money / i);
  money %= i;
}
console.log(result);
